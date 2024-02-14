from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboard_markup.keyboard import check_yes_no, keybord_start, kb_remove
from push.push_notify import main_push

class NotifyAdd(StatesGroup):
    
    time_interval = State()
    comment = State()
    check = State()


async def start_register(message: types.Message, state: FSMContext):
    
    await NotifyAdd.time_interval.set()
    await message.answer(text= "Укажите время (Формат: час мин. \nПример: 2 11, 15 6)\nЕсли только минуты (Формат: мин. \nПример: 22, 8)", reply_markup= kb_remove)
    

async def reg_time_interval(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        data['time_interval'] = message.text
        
        time_inter = data['time_interval'].split(" ")

        if len(time_inter) == 1:
            
            try:
                if ((int(time_inter[0]) <= 59) and (int(time_inter[0]) >= 1)):
                    
                    data['time_interval'] = int(time_inter[0]) * 60
                    
                    await NotifyAdd.comment.set()
                    await message.answer(text= "Текст напоминания: ")

                else:
                    await message.answer(text= "Не может быть больше 59 мин. и меньше 1 мин.", reply_markup= await keybord_start())
                    await state.finish()

                    return
            except:
                await message.answer(text= "Ошибка при вводе. Попробуйте ещё раз!", reply_markup= await keybord_start())
                await state.finish()
                
                return
        
        elif len(time_inter) == 2:
            
            try:
                if ((int(time_inter[0]) <= 23) and (int(time_inter[0]) >= 1)) and ((int(time_inter[1]) <= 59) and (int(time_inter[1]) >= 1)):
                    
                    data['time_interval'] = (int(time_inter[0]) * 60 * 60) + (int(time_inter[1]) * 60)
                    
                    await NotifyAdd.comment.set()
                    await message.answer(text= "Текст напоминания: ")

                else:
                    await message.answer(text= "Не может быть больше 59 мин. и меньше 1 мин. А также больше 23 час. и меньше 1 час.", reply_markup= await keybord_start())
                    await state.finish()

                    return
            except:
                await message.answer(text= "Ошибка при вводе. Попробуйте ещё раз!", reply_markup= await keybord_start())
                await state.finish()
                
                return
            
        else:
            await message.answer(text= "Ошибка при вводе. Попробуйте ещё раз!", reply_markup= await keybord_start())
            await state.finish()
            
            return
        

async def reg_comment(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        data['comment'] = message.text
        
        await NotifyAdd.check.set()
        await message.answer(text= "Всё верно?", reply_markup= await check_yes_no())


async def reg_check(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        data['check'] = message.text
        
        if data['check'] == "Да ✅":
            
            await main_push(message.chat.id, data['time_interval'], data['comment'])
            
            await message.answer(text= "Напоминание установлено", reply_markup= await keybord_start())
            await state.finish()
            
            return
        
        elif data['check'] == "Нет ❌":
            
            await message.answer(text= "Отмена напоминания!", reply_markup= await keybord_start())
            await state.finish()
            
            return

 
def start_notify_add(dp: Dispatcher):
    
    dp.register_message_handler(start_register, Text(equals="Своё время ⏳"), state=None)
    dp.register_message_handler(reg_time_interval, state=NotifyAdd.time_interval)
    dp.register_message_handler(reg_comment, state=NotifyAdd.comment)
    dp.register_message_handler(reg_check, state=NotifyAdd.check)