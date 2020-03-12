"""
Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое чаще других встречается в массиве. Ограничение времени: 2 с, ограничение памяти: 256 МБ.

Формат ввода
В первой строке входных данных записано число n (1 ≤ n ≤ 300 000).
Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1 000 000 000).

Формат вывода
Выведите единственное число x, наибольшее из чисел, которое чаще других встречается в массиве a.
"""
import time
import random

maxs = 0
element = None
x = 100
a = [random.randint(0, 1000) for i in range(0, x)]
start = time.time()
slovar = dict()
for i in a:
    slovar[i] = slovar.get(i, 0) + 1
    print(i, slovar[i], element, maxs)
    if slovar[i] > maxs or slovar[i] == maxs and i > element:
        maxs = slovar[i]
        element = i
print(element, maxs, slovar[element])
print(time.time() - start)
