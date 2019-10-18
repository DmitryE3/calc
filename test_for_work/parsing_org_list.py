"""
Написать модуль на python, который получает с сайта list-org описание компании.
Входные данные: ссылка на компанию (например https://www.list-org.com/company/4868135)
Выходные данные: таблица , в каждой строке которой должны находиться:
Полное юридическое наименование, Руководитель, Дата регистрации, Статус, ИНН, КПП, ОГРН,
"""
import re
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

#Создаем soup файл в котором будем искать информацию
def make_soup(url):
    #url = 'https://www.list-org.com/company/4868135'
    html_file = urlopen(url).read()
    soup_file = BS(html_file, 'html5lib')
    return soup_file

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
def printing(url):
    for i in find_info(make_soup(url)):
        print(i)


def main():
    url = input('Введите URL: ')
    printing(url)


if __name__ == '__main__':
    main()