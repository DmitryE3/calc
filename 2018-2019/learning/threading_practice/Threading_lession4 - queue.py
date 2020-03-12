# Модуль Queue
# Класс Queue реализует в себе все необходимые блокировки для синхронизации процессов

import queue
import threading
import time


def putting_thread(q):
    while True:
        print('Start thread')
        time.sleep(10)
        q.put(5)
        print('sup something')


q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q,), daemon=True)
t.start()
q.put(0)
print(q.get(), 'first item')
print('-----')
print(q.get(), 'finish')

# q.put(5) #добавляем в очередь 5
# print(q.get()) #получаем из очереди 5, очередь становится пуста
# print(q.empty()) #проверка на пустоту
# for i in range(5):
#    q.put(i)
# while not q.empty():
#   print(q.get(),end=' ')
