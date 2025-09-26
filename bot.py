<<<<<<< HEAD
import telebot
import requests

# 🔐 Telegram bot sozlamalari
BOT_TOKEN = "8409191752:AAEgPddZfKIGrFHOSfBnY6OfQTCk3aRHMzo"
ADMIN_CHAT_ID = "5167278754"  # Dostonbek — Azamov.B

# 🌐 Backend URL (Render.com’dagi)
BACKEND_URL = "https://baxaoptom-backend.onrender.com"

bot = telebot.TeleBot(BOT_TOKEN)

# 🧩 Mini App tugmasi
webAppButton = telebot.types.WebAppInfo(url="https://baxaoptom-miniapp.vercel.app")  # Frontend URL
mainMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(telebot.types.KeyboardButton("🛍 Buyurtma berish", web_app=webAppButton))

# 🟢 Bot ishga tushganda
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Salom! BaxaOptom’ga xush kelibsiz.", reply_markup=mainMenu)

# 📩 Buyurtma yuborish (Mini App’dan)
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app(message):
    try:
        data = message.web_app_data.data
        order = eval(data)  # JSON string → dict

        # 🔗 Backendga yuborish
        response = requests.post(f"{BACKEND_URL}/order", json=order)
        if response.status_code == 200:
            bot.send_message(message.chat.id, "✅ Buyurtma qabul qilindi!")
        else:
            bot.send_message(message.chat.id, "❌ Xatolik: buyurtma yuborilmadi.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Xatolik: {str(e)}")

# 🚀 Botni ishga tushirish
=======
import telebot
import requests

# 🔐 Telegram bot sozlamalari
BOT_TOKEN = "8409191752:AAEgPddZfKIGrFHOSfBnY6OfQTCk3aRHMzo"
ADMIN_CHAT_ID = "5167278754"  # Dostonbek — Azamov.B

# 🌐 Backend URL (Render.com’dagi)
BACKEND_URL = "https://baxaoptom-backend.onrender.com"

bot = telebot.TeleBot(BOT_TOKEN)

# 🧩 Mini App tugmasi
webAppButton = telebot.types.WebAppInfo(url="https://baxaoptom-miniapp.vercel.app")  # Frontend URL
mainMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(telebot.types.KeyboardButton("🛍 Buyurtma berish", web_app=webAppButton))

# 🟢 Bot ishga tushganda
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Salom! BaxaOptom’ga xush kelibsiz.", reply_markup=mainMenu)

# 📩 Buyurtma yuborish (Mini App’dan)
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app(message):
    try:
        data = message.web_app_data.data
        order = eval(data)  # JSON string → dict

        # 🔗 Backendga yuborish
        response = requests.post(f"{BACKEND_URL}/order", json=order)
        if response.status_code == 200:
            bot.send_message(message.chat.id, "✅ Buyurtma qabul qilindi!")
        else:
            bot.send_message(message.chat.id, "❌ Xatolik: buyurtma yuborilmadi.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Xatolik: {str(e)}")

# 🚀 Botni ishga tushirish
>>>>>>> 72c5b9f (Add full backend with bot.py)
bot.polling()