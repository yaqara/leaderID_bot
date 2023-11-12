from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
import logging, asyncio

from keyboard import authKeyboard, webKeyboard

import aiohttp
from selenium import webdriver
from selenium.webdriver.common.by import By
from aioselenium import Remote

from security import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
# async def web_app_handler(msg):
#     print(msg)

# async def get_driver():
#     async with aiohttp.ClientSession() as session:
#         remote = await Remote.create(command_executor="http://localhost:9515/wd/hub", desired_capabilities={"browserName": "firefox"}, session=session)
#         async with remote as driver:
#             await driver.get("https://leader-id.ru/")
#             return driver

@dp.message_handler(commands=["start"])
async def start_msg(msg: types.Message):
    await msg.answer(
        "Здравствуйте, выберите из списка, есть ли у вас аккаунт на leader-id.ru или нет",
        reply_markup = authKeyboard()
        )

@dp.callback_query_handler(lambda c: c.data=="regPressed" or c.data=="loginPressed")
async def regAlg(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == 1012091973:
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text="Нажми на кнопку ниже, чтобы поделиться своим контактом.",
            reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton("Поделиться контактом", request_contact=True)]
            ], resize_keyboard=True)
            )

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def auth(msg: types.Message):
    if msg.from_user.id == 1012091973:
        async def authUser():
            async def checkAuth():
                driver.switch_to.window(driver.window_handles[0])
                if driver.current_url == "https://leader-id.ru/profile":
                    await msg.reply("Вы успешно зарегистрированы", reply_markup=webKeyboard())
                else:
                    await asyncio.sleep(2)
                    await checkAuth()
            driver = webdriver.Firefox()
            driver.get("https://leader-id.ru/")
            driver.find_element(By.CSS_SELECTOR, "._20JsdZWnuYjL > svg:nth-child(1)").click()
            driver.find_element(By.CSS_SELECTOR, ".app-icon-button > svg:nth-child(1)").click()
            while True:
                try:
                    iframe = driver.find_element(By.CSS_SELECTOR, "#telegram-login-Leader_ID_Auth_Bot")
                    break
                except: await asyncio.sleep(1)
            driver.switch_to.frame(iframe)
            await asyncio.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".btn").click()
            driver.switch_to.window(driver.window_handles[1])
            while True:
                try: 
                    print(1)
                    driver.find_element(By.CSS_SELECTOR, "#login-phone").send_keys(msg.contact.phone_number[2:])
                    break
                except: await asyncio.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "button.button-item:nth-child(2)").click()
            await msg.answer("Просмотрите сообщения от Telegram и продтвердите вход")
            await checkAuth()
        await authUser()        

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())