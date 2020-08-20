import telebot
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from links import pattern_folder, telebot_id


bot = telebot.TeleBot(telebot_id)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
folder = pattern_folder


def parser(element):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    dict_collection = {}
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=1000, fields="nextPageToken, files(id, name, webViewLink)", q=folder).execute()
    items = results.get('files', [])
    if items:
        for item in items:
            if element.lower() in item['name'].lower():
                dict_collection[item['name']] = item['webViewLink']
    return dict_collection


@bot.message_handler(content_types=['text'])
def start_message(message):
    result = parser(message.text)
    if result:
        for name, link in result.items():
            bot.send_message(message.chat.id, name)
            bot.send_message(message.chat.id, link)


bot.polling()