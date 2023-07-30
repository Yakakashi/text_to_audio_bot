import telebot
from telebot import types
from gtts import gTTS
from langdetect import detect

TOKEN = "##########:###################################"

f1 = """/start - приветствие
Для перевода текста в аудио просто отправьте сообщение в данный бот."""

bot = telebot.TeleBot(TOKEN)
language = "ru"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я бот для перевода текстовых сообщений в аудиосообщения")
    bot.send_message(message.chat.id, f1)

@bot.message_handler(content_types=["text"])
def convert(message):
    string = gTTS(text=message.text, lang= detect(message.text))
    string.save("res_audio.mp3")
    bot.send_audio(message.chat.id, open("res_audio.mp3", "rb"))
bot.polling(none_stop=True)