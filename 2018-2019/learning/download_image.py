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


def downloader1(link_img, num_img):
    img = urlopen(link_img).read()
    with open('img{}.jpg'.format(num_img + 1), 'wb') as img_file:
        img_file.write(img)
    print('Potok ' + str(num_img + 1) + ' zakonchil zagruzku ' + link_img)

def downloader(link_img, num):
    try:
        image = urlopen(link_img)
        print('Potok '+str(num+1)+' zakonchil zagruzku '+link_img)
    except:
        print('error')


#url = str(input())
url = 'https://hh.ru/'
f_html = urlopen(url)
f_str = f_html.read()
f_str = f_str.decode('utf-8')
#find_img = set(re.findall(r'src="(.+?)"', f_str))
#find_img = re.findall(r'<img(.*?)</img>', f_str)
p = re.compile(r'<img\s+[^>]* ?src="(\w+[^>]*?)"', re.IGNORECASE)
find_img = p.findall(f_str)
images = []
for i in find_img:
    if re.match('http', i):
        images.append(i)
for num, link in enumerate(images):
    print(str(num + 1) + ' izobrazhenie ' + link)
    my_thread = threading.Thread(target=downloader, args=(link, num,))
    my_thread.start()
for i in range(len(images)):
    my_thread.join()
