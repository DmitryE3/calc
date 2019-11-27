import telebot
import os
import re

bot = telebot.TeleBot('1054467570:AAHTOT3ZxTo01yqh6JTZp4vc4Zxta5xmvzo')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'Привет, ты ищешь {},'
                                      ' сейчас я покажу все, что есть в коллекции'.format(message.text))
    directory = r'/home/oi/Python_repos/calc/learning/telegram_collection_bot/collection/'
    name = os.listdir(directory)
    pics = []
    pattern = re.compile(message.text.lower() + '\w+\.\w+')
    for i in name:
        x = pattern.search(i)
        if x:
            pics.append(x.group())
    for pic in pics:
        bot.send_photo(message.chat.id, photo=open(directory+pic, 'rb'))


bot.polling()

