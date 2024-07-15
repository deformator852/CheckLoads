from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = "7122908765:AAFQCJwn-_0Rtn6GBp5hbOxi8SoYiLauTZg"
ROOT_ADMIN = 6432444926
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
