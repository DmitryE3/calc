import telebot
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from telebot import apihelper

apihelper.proxy = {'socks5h': 'socks5://telegram.vpn.net:55555'}

bot = telebot.TeleBot('')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
folder = ""
folder_2 = ""
DICT_COLLECTION = {}

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Обновить базу коллекции')

def parser():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    dict_collection = dict()
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Не получается спарсить более 460 файлов с папки, добавлена дополнительная папка
    folders = [folder, folder_2]
    for i in folders:
        results = service.files().list(pageSize=1000,
                                       fields="nextPageToken, files(id, name, webViewLink)",
                                       q=f"{i} in parents").execute()
        items = results.get('files', [])
        if items:
            for item in items:
                dict_collection[item['name']] = item['webViewLink']

    return dict_collection


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот запущен, обновите базу', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global DICT_COLLECTION
    if message.text == 'Обновить базу коллекции':
        DICT_COLLECTION = parser()
        bot.send_message(message.chat.id, 'База обновлена', reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, 'Привет, ты ищешь {},'
                                          ' сейчас я покажу все, что есть в коллекции'.format(message.text))
        pics = []
        names = DICT_COLLECTION.keys()
        find_this = message.text.lower()
        for name in names:
            if find_this in name.lower():
                pics.append(name)
        if len(pics) == 0:
            bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')
        else:
            bot.send_message(message.chat.id, ' Найдено ' + str(len(pics)))
            for pic in pics:
                bot.send_message(message.chat.id, pic)
                bot.send_message(message.chat.id, DICT_COLLECTION[pic])


bot.polling()

