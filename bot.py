from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils import executor
import logging

# 🔐 Bot token
BOT_TOKEN = "8409191752:AAEgPddZfKIGrFHOSfBnY6OfQTCk3aRHMzo"

# 🔧 Loglar
logging.basicConfig(level=logging.INFO)

# 🤖 Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🛍 Faqat bitta tugma — Magazin
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton(
    text="🛍 Magazin",
    web_app=WebAppInfo(url="https://baxabet04.github.io/baxaoptom_miniapp/")  # GitHub Pages versiyasi
))

# 👋 Start komandasi
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer(
        "👋 BaxaOptom botga xush kelibsiz!\n\n🛍 Magazin tugmasini bosib katalogni ko‘ring.",
        reply_markup=keyboard
    )

# 🚀 Botni ishga tushirish
if __name__ == '__main__':
    try:
        print("✅ BaxaOptom bot ishga tushdi...")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"❌ Xatolik: {e}")