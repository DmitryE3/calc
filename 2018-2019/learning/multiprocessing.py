import os
import requests

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Lock


def get_req(url, blocker):
    #Захватываем блокер
    blocker.acquire()
    try:
        #Получаем ИД процесса
        proc = os.getpid()
        res = requests.get(url)
        #Получаем имя текущего процесса
        proc_name = current_process().name
        print(res, proc, proc_name)
    finally:
        # Отпускаем блокер
        blocker.release()


if __name__ == '__main__':
    blocker = Lock()
    urls = ['https://www.djangoproject.com/weblog/?page={}'.format(i) for i in range(1, 5)]
    proc_names = ['Proc name {}'.format(i) for i in range(1, 5)]
    procs = []

    for i, url in enumerate(urls):
        proc = Process(target=get_req, name=proc_names[i], args=(url, blocker,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
