from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted, TelegramAPIError, NetworkError, RetryAfter
from aiohttp.client_exceptions import ClientOSError, ClientConnectorError
from asyncio.exceptions import TimeoutError
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import TOKEN, admin
from keyboard_markup.keyboard import keybord_start, keyboard_inline_notify, keyboard_my_time, kb_remove
from display.display_notify import start_notify_add
from display.display_inline5m import start_inline_add5m
from display.display_inline10m import start_inline_add10m
from display.display_inline15m import start_inline_add15m
from display.display_inline30m import start_inline_add30m
from display.display_inline1h import start_inline_add1h
from display.display_inline3h import start_inline_add3h
from display.display_inline6h import start_inline_add6h
from display.display_inline1d import start_inline_add1d

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

print("Бот запущен!")
print("Напоминалка | Бот-уведомлений")

start_notify_add(dp)


@dp.message_handler(commands=["start", "update"])
async def start(message: types.Message):
    
    await message.answer(text= "Добро пожаловать в Напоминалку!", reply_markup= await keybord_start())
    

@dp.message_handler(text=["⏱ Напомнить ⏱"])
async def notify(message: types.Message):
    
    await message.answer(text= "Выберите время", reply_markup= await keyboard_inline_notify())
    
    await message.answer(text= "Ввести своё время", reply_markup= await keyboard_my_time())


@dp.message_handler(text=["📝 Мои заметки 📝"])
async def notify(message: types.Message):
    
    await message.answer(text= "В разработке")
    

@dp.message_handler(text=["⬅️ Назад"])
async def notify(message: types.Message):
    
    await message.answer(text= "Главное меню", reply_markup= await keybord_start())
    

@dp.callback_query_handler()
async def note_date_time(callback: types.CallbackQuery):
    
    if callback.data == "5m":
        
        await callback.answer(text= "5 мин")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add5m(dp)
        
    elif callback.data == "10m":
        
        await callback.answer(text= "10 мин")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add10m(dp)
        
    elif callback.data == "15m":
        
        await callback.answer(text= "15 мин")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add15m(dp)
        
    elif callback.data == "30m":
        
        await callback.answer(text= "30 мин")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add30m(dp)
        
    elif callback.data == "1h":
        
        await callback.answer(text= "1 час")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add1h(dp)
        
    elif callback.data == "3h":
        
        await callback.answer(text= "3 час")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add3h(dp)
        
    elif callback.data == "6h":
        
        await callback.answer(text= "6 час")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add6h(dp)
        
    elif callback.data == "1d":
        
        await callback.answer(text= "1 день")
        await callback.message.answer(text= "Текст напоминания: ", reply_markup= kb_remove)
        await start_inline_add1d(dp)
        

@dp.message_handler()
async def del_text(message: types.Message):
    
    await message.delete()
    
@dp.errors_handler(exception=TimeoutError)
async def error_oserror(update: types.Update, exception: TimeoutError):
    
    if isinstance(exception, TimeoutError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
    
    return True

@dp.errors_handler(exception=OSError)
async def error_oserror(update: types.Update, exception: OSError):
    
    if isinstance(exception, OSError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
    
    return True

@dp.errors_handler(exception=NetworkError)
async def error_oserror(update: types.Update, exception: NetworkError):
        
    if isinstance(exception, NetworkError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=TelegramAPIError)
async def error_oserror(update: types.Update, exception: TelegramAPIError):
    
    if isinstance(exception, TelegramAPIError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=ClientOSError)
async def error_oserror(update: types.Update, exception: ClientOSError):
    
    if isinstance(exception, TelegramAPIError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=ClientConnectorError)
async def error_oserror(update: types.Update, exception: ClientConnectorError):  
    
    if isinstance(exception, TelegramAPIError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=RetryAfter)
async def exception_handler(message: types.Message, update: types.Update, exception: RetryAfter):
    
    await bot.send_message(message.chat.id, text="Не флудите!")
    
    return True

if __name__ == "__main__":
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except:
            print("Любая ошибка")
    