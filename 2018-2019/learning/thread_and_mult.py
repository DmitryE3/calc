"""Используя библиотеки threading или multiprocessing, осуществить поиск с использованием регулярных выражений по
новостной ленте сайта https://www.djangoproject.com/weblog/ количества словосочетаний Django 2.0. На ввод
 данных подается адрес новостной ленты и число потоков или процессов через пробел, например:
https://www.djangoproject.com/weblog/ 10
вывод осуществляется числом, например:
14

Пример входных данных:
https://www.djangoproject.com/weblog/ 10
Пример выходных данных:
14 """

import re
import threading
from multiprocessing import Queue
from multiprocessing import Process
from urllib.request import urlopen


def find_word(number):
    place_url = url + '?page={}'.format(number)
    f_url = urlopen(place_url)
    f_str = f_url.read().decode('utf-8')
    q.put(len(pattern.findall(f_str)))


x = 'https://www.djangoproject.com/weblog/ 10'
url, nums = x.split()
pattern = re.compile(r'Django 2.0')
counter = 0
#threads = []
all_processes = []
q = Queue()

for i in range(int(nums)):
    my_process = Process(target=find_word, args=(i+1,))
    all_processes.append(my_process)
    my_process.start()
#    my_thread = threading.Thread(target=find_word, args=(i+1,))
#    threads.append(my_thread)
#    my_thread.start()

for i in all_processes:
    i.join()

#for thread in threads:
#    thread.join()
while not q.empty():
    counter += q.get()

print(counter)

