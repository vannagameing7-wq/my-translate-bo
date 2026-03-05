import telebot
import requests

# បំពេញលេខកូដរបស់អ្នក
BOT_TOKEN = "8700911999:AAEEet6lamvn5uATcQWglRuHWiuTO50exX0"
GEMINI_API_KEY = "AizaSyaA-S-O2xN1UcKgZ-a-TkoGHfc6ZR2Uxqg"

bot = telebot.TeleBot(BOT_TOKEN)

def translate_to_en(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": f"Translate this Khmer text to English: {text}"}]}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        return f"Error: {response.status_code}"
    except:
        return "មានបញ្ហាភ្ជាប់ទៅ AI"

@bot.message_handler(func=lambda message: True)
def handle(message):
    answer = translate_to_en(message.text)
    bot.reply_to(message, answer)

print("Bot is running...")
bot.infinity_polling()
