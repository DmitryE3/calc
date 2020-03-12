"""
Написать модуль на python, который получает с сайта list-org описание компании.
Входные данные: ссылка на компанию (например https://www.list-org.com/company/4868135)
Выходные данные: таблица , в каждой строке которой должны находиться:
Полное юридическое наименование, Руководитель, Дата регистрации, Статус, ИНН, КПП, ОГРН,
"""
import re
import time
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen


# Создаем soup файл в котором будем искать информацию
def make_soup():
    url = 'https://www.list-org.com/company/4868135'
    html_file = urlopen(url).read()
    soup_file = BS(html_file, 'html5lib')
    return soup_file
    # print(soup_file.prettify())


# def find_info_second(soup_file):
#     name = soup_file.find('a', {'class': 'upper'}).text
#     boss = soup_file.find('a', {'title': re.compile(r'^все данные о')}).text
#     date = soup_file.find(text=re.compile(r'\d{2}\.\d{2}\.\d{4}'))
#     status = soup_file.find('td', {'class': 'status_1'}).text
#     inn = soup_file.find('title').text
#     inn = re.findall(r'ИНН:(\d+)', inn)[0]
#     # Сомнительный метод поиска КПП, надо подумать лучше
#     kpp = soup_file.find(text=re.compile(r'{} / \d+'.format(inn)))
#     kpp = kpp.split(' / ')[1]
#     meta = soup_file.find('meta', {'name': 'description'})
#     n = meta.get('content')
#     ogrn = re.findall(r'ОГРН:\s?(\d+)', n)[0]
#     return [name, boss, date, status, inn, kpp, ogrn]


# Поиск требуемой инфы
def find_info(soup_file):
    info = soup_file.findAll('div', 'c2m')
    name = info[0].p.a.text
    list_td = info[0].table.findAll(['td'])
    boss = list_td[1].text
    inn, kpp = list_td[3].text.split(' / ')
    start_date = list_td[11].text
    status = list_td[13].text
    find_ogrn = info[2].findAll(['p'])
    ogrn = re.search(r'\d+', str(find_ogrn[3]))
    return [name, boss, start_date, status, inn, kpp, ogrn.group()]


# Вывод информации на экран
def printing():
    for i in find_info(make_soup()):
        print(i)


def main():
    #     url = input('Введите URL: ')
    start_time = time.time()
    printing()
    print('Время выполнения - ', time.time() - start_time)


if __name__ == '__main__':
    main()
