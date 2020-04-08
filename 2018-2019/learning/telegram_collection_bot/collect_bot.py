import telebot
import os
import re
# from telebot import apihelper
# apihelper.proxy = {'https': 'socks5://telegram.vpn.net:55555'}

bot = telebot.TeleBot('')
# тестовый словарь
dict_collection = {'jack pott' : ['https://sun6-13.userapi.com/XhaZtgH3k_UN1HOCBFaHJU24UWVZ1s5ZT_L_MA/wosCN6IQ8T4.jpg',
                                  'https://sun6-19.userapi.com/poIOzY9ezy_kfQ8bPujte5-fyyssBLhTZKZmxw/PhwnQAeChh4.jpg']}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'Привет, ты ищешь {},'
                                      ' сейчас я покажу все, что есть в коллекции'.format(message.text))
    pics = []
    names = dict_collection.keys()
    find_this = message.text.lower()
    for name in names:
        if find_this in name.lower():
            pics.append(name)
    if len(pics) == 0:
        bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')
    else:
        for pic in pics:
            # bot.send_photo(message.chat.id, photo=open(directory + pic, 'rb'))
            bot.send_message(message.chat.id, ' Найдено ' + str(len(pics)))
            for i in dict_collection[pic]:
                bot.send_photo(message.chat.id, photo=i)


bot.polling()

