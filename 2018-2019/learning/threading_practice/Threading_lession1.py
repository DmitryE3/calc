"""Запустим несколько процессов одновременно"""

import threading
import time


def sleeper(sec, name):
    print('Привет,я {}, я собираюсь поспать {} секунд'.format(name, sec))
    time.sleep(sec)
    print('{} проснулся'.format(name))


process_list = []

start = time.time()
for i in range(5):
    process = threading.Thread(target=sleeper, name='Thread{}'.format(i), args=(5 + i, 'Thread{}'.format(i)))
    process_list.append(process)
    process.start()

for j in process_list:
    j.join()

end = time.time()
print('time was {}'.format(end - start))
