from aiogram import Bot
from config.config import TOKEN
import asyncio
import time

bot = Bot(token=TOKEN)

async def push_time(users, time_interval, comment):
    time_time = time.time() + 10800
    time_now = time.strftime("Дата: %d/%m/%Y Время: %H:%M:%S", time.gmtime(time_time))
    time_format = time.strftime("%H:%M:%S", time.gmtime(time_interval))
    time_come = time.strftime("Дата: %d/%m/%Y Время: %H:%M:%S", time.gmtime(time_time + time_interval))
    print(users, "Время :-", time_format, comment, "| Назначил -", time_now)
    
    await bot.send_message(chat_id= users, text= f"Напоминание придет в {time_come}")
    
    await asyncio.sleep(time_interval)
    
    await bot.send_message(chat_id= users, text= f"Напоминание: {comment}")
    
    
async def main_push(users, time_interval, comment):
    
    _ = asyncio.create_task(push_time(users, time_interval, comment))
    
    return