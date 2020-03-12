"""Написать модуль на python, который получает с сайта https://habr.com/ru/ самые популярные посты за год.
Входные данные: число count - количество получаемых постов
Выходные данные: таблица , в каждой строке которой должны находиться:
заголовок поста, короткое описание поста, дата публикации, имя автора поста
"""
import re
import csv
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen


def find_info_about_post(post):
    preview = post.find('ul', 'post__hubs inline-list').text
    a = re.compile(r'\s\s+(.+),?\n')
    preview = a.findall(preview)
    preview = preview[:-1]
    #Если под коротким описанием имеется ввиду начало поста
    #preview = post.find('div', 'post__text post__text-html js-mediator-article').text
    time = post.find('span', 'post__time').text
    autor = post.find('span', 'user-info__nickname user-info__nickname_small').text
    title = post.h2.a.text
    return [title, preview, time, autor]


def get_posts(page_counter):
    try:
        url = 'https://habr.com/ru/top/yearly/page{}/'.format(page_counter)
        html_file = urlopen(url).read()
        soup_file = BS(html_file, 'html5lib')
        posts.extend(soup_file.findAll('li', id=re.compile('post')))
        if len(posts) < POST_COUNTER:
            page_counter += 1
            return get_posts(page_counter)
        else:
            return posts
    except:
        print('Нужного количества постов в этом году нет')


# Для удобного вывода в виде csv таблицы
def make_csv_table(posts):
    infos = []
    for i in range(POST_COUNTER):
        infos.append(find_info_about_post(posts[i]))
    with open('infos.csv', 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(infos)


def printing(posts):
    for i in range(POST_COUNTER):
        for j in find_info_about_post(posts[i]):
            if type(j) is list:
                print(*j)
            else:
                print(j)


posts = []
page_counter = 0
POST_COUNTER = int(input('Введите нужное количество постов: '))
posts = get_posts(page_counter)
printing(posts)
