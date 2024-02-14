from aiogram import types

kb_remove = types.ReplyKeyboardRemove()

async def keybord_start():
    
    kb_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_notify = types.KeyboardButton("⏱ Напомнить ⏱")
    kb_my_notes = types.KeyboardButton("📝 Мои заметки 📝")
    kb_start.add(kb_notify, kb_my_notes)
    
    return kb_start


async def keyboard_inline_notify():
    
    kb_start_inline = types.InlineKeyboardMarkup(row_width=4, resize_keyboard=True)
    kb_5 = types.InlineKeyboardButton(text= "5 мин", callback_data= "5m")
    kb_10 = types.InlineKeyboardButton(text= "10 мин", callback_data= "10m")
    kb_15 = types.InlineKeyboardButton(text= "15 мин", callback_data= "15m")
    kb_30 = types.InlineKeyboardButton(text= "30 мин", callback_data= "30m")
    kb_start_inline.add(kb_5, kb_10, kb_15, kb_30)
    kb_1 = types.InlineKeyboardButton(text= "1 час", callback_data= "1h")
    kb_3 = types.InlineKeyboardButton(text= "3 час", callback_data= "3h")
    kb_6 = types.InlineKeyboardButton(text= "6 час", callback_data= "6h")
    kb_1d = types.InlineKeyboardButton(text= "1 день", callback_data= "1d")
    kb_start_inline.add(kb_1, kb_3, kb_6, kb_1d)
    
    return kb_start_inline


async def keyboard_my_time():
    
    kb_start_my_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_my_time = types.KeyboardButton("Своё время ⏳")
    kb_back = types.KeyboardButton("⬅️ Назад")
    kb_start_my_time.add(kb_my_time, kb_back)
    
    return kb_start_my_time


async def check_yes_no():
    
    kb_start_check = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_yes = types.KeyboardButton("Да ✅")
    kb_no = types.KeyboardButton("Нет ❌")
    kb_start_check.add(kb_yes, kb_no)
    
    return kb_start_check