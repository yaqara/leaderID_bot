from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
import logging, asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from security import TOKEN


dp = Dispatcher()

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_handler(msg):
    print(msg)

@dp.message_handler(commands=["start"])
async def start_msg(msg: types.Message):
    await msg.answer("Привет")

@dp.message_handler(commands=["reg"])
async def reg_msg(message: types.Message):
    
    
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())