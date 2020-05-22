import telebot
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from telebot import apihelper

apihelper.proxy = {'socks5h': 'socks5://telegram.vpn.net:55555'}

bot = telebot.TeleBot('1054467570:AAHTOT3ZxTo01yqh6JTZp4vc4Zxta5xmvzo')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
folder = '1InPQkzJHuCYkv_Rv9WZHaHEDHVKlsmz_'
folder_2 = '1hmK7ajFYAt4_ZBRbyImqKuEyHLMKBY_j'
DICT_COLLECTION = {}


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
    results = service.files().list(
        pageSize=1000,
        fields="nextPageToken, files(id, name, webViewLink,  parents, createdTime)",
        q="'1InPQkzJHuCYkv_Rv9WZHaHEDHVKlsmz_' in parents").execute()

    results2 = service.files().list(
        pageSize=1000,
        fields="nextPageToken, files(id, name, webViewLink,  parents, createdTime)",
        q="'1hmK7ajFYAt4_ZBRbyImqKuEyHLMKBY_j' in parents").execute()

    res = [results, results2]

    for i in res:
        items = i.get('files', [])
        if not items:
            pass
        else:
            for item in items:
                dict_collection[item['name']] = item['webViewLink']
    return dict_collection


DC = parser()
print(sorted(DC.keys()))
print(len(DC.keys()))
