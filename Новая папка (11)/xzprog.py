import telebot
import requests
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo

bot = telebot.TeleBot("7317806863:AAGj66MBxRx3JxkPgIyDnKKOvoKiB4J04hw")

@bot.message_handler(commands=["start"])
def hand(message):
   reply = InlineKeyboardMarkup()
   btn1 = InlineKeyboardButton("Заходи на веб сайт :) ",web_app=WebAppInfo(url="https://www.youtube.com/?app=desktop&hl=ru"))
   reply.add(btn1)
   bot.send_message(message.chat.id,"Давай",reply_markup=reply)

bot.polling()