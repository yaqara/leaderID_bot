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
    await message.reply("Привет! Нажми на кнопку ниже, чтобы поделиться своим контактом.",
                        reply_markup=types.ReplyKeyboardMarkup(
                            keyboard=[
                                [types.KeyboardButton("Поделиться контактом", request_contact=True)]
                        ], resize_keyboard=True))

@dp.message(types.ContentType.CONTACT)
async def get_contact(msg: types.Message):
    async def reg():
        driver = webdriver.Firefox()
        driver.get()
        driver.find_element(By.CSS_SELECTOR, "._20JsdZWnuYjL > svg:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, ".app-icon-button > svg:nth-child(1)").click()
        sleep(2)
        iframe = driver.find_element(By.CSS_SELECTOR, "#telegram-login-Leader_ID_Auth_Bot")
        driver.switch_to.frame(iframe)
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        driver.switch_to.window(driver.window_handles[1])
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#login-phone").send_keys(tel)
        driver.find_element(By.CSS_SELECTOR, "button.button-item:nth-child(2)").click()
    await msg.answer("Просмотрите сообщения от Telegram и продтвердите вход")
    
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
