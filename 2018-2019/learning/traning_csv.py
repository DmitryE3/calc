# Практика работы с CSV. Создадим csv файл со списком линков на изображения на сайте хх.ру
import csv
import re
import os
from urllib.request import urlopen


def writer_csv(file, info):
    with open(file, 'w', newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(info)


def reader_csv(file):
    with open(file, 'r', newline='') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            print(row[0], '-', row[1])


def url_to_str(url):
    f_url = urlopen(url)
    f_str = f_url.read().decode('utf-8')
    return f_str


def find_img(f_str):
    pattern = re.compile(r'<img\s+[^>]*?src="(\w+[^>]*?)"', re.IGNORECASE)
    images = pattern.findall(f_str)
    return images


filename = 'images_link.csv'
url = 'https://wwww.hh.ru/'
numerate_list = []
for num, link in enumerate(find_img(url_to_str(url))):
    numerate_list.append([num+1, link])
writer_csv(filename, numerate_list)
reader_csv(filename)
os.remove(filename)