from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard_markup.keyboard import check_yes_no, keybord_start
from push.push_notify import main_push

class NotifyInlineAdd6h(StatesGroup):
    
    comment = State()
    check = State()
        

async def reg_comment(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        data['comment'] = message.text
        
        await NotifyInlineAdd6h.check.set()
        await message.answer(text= "Всё верно?", reply_markup= await check_yes_no())


async def reg_check(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        data['check'] = message.text
        
        if data['check'] == "Да ✅":
            
            time_interval_6h = 6 * 60 * 60
            
            await main_push(message.chat.id, time_interval_6h, data['comment'])
            
            await message.answer(text= "Напоминание установлено", reply_markup= await keybord_start())
            await state.finish()
            
            return
        
        elif data['check'] == "Нет ❌":
            
            await message.answer(text= "Отмена напоминания!", reply_markup= await keybord_start())
            await state.finish()
            
            return

 
async def start_inline_add6h(dp: Dispatcher):
    
    await NotifyInlineAdd6h.comment.set()
    
    dp.register_message_handler(reg_comment, state=NotifyInlineAdd6h.comment)
    dp.register_message_handler(reg_check, state=NotifyInlineAdd6h.check)