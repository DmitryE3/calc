"""
1. Осуществить ввод адреса Интернет-страницы.
2. Осуществить поиск всех изображений на странице.
3. Удалить дубликаты.
4. Удалить адреса без http или https.
5. Вывести адреса изображений с нумерацией, нумерацию изображений начинать с 1.
6. Потоками осуществить загрузку изображений и информацию о загрузке вывести на экран отдельными строками
7. В случае невозможности загрузки выводить 'error'.

Пример входных данных:
https://ya.ru/

Пример выходных данных:
1 izobrazhenie https://mc.yandex.ru/watch/723233
Potok 1 zakonchil zagruzku https://mc.yandex.ru/watch/723233
"""
import threading
import re
from urllib.request import urlopen

# Тут будет функция для скачивания
def downloader():
    pass


#url = str(input())
url = 'https://hh.ru/'
f_html = urlopen(url)
f_str = f_html.read()
f_str = f_str.decode('utf-8')
#f_bs = BS(f_str, 'lxml')
#print(f_bs.find_all('img'))
find_img = set(re.findall(r'src="(.+?)"', f_str))
images = []
for i in find_img:
    if re.match('http', i):
        images.append(i)
print(len(images))
for i in range(len(images)):
    print(str(i+1)+' izobrazhenie '+images[i])
    