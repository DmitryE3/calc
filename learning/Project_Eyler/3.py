"""Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""
from math import sqrt


def erastofen(count, mnozhestvo):
    for i in mnozhestvo:
        print(i)
        if i != mnozhestvo[count] and i % mnozhestvo[count] == 0:
            mnozhestvo.remove(i)
    try:
        erastofen(count + 1, mnozhestvo)
    except:
        print('x')
    return mnozhestvo


number = int(input('Введите ваше число, а мы найдем самый большой простой делитель - '))
lst = [i for i in range(1, int(sqrt(number)))]
list_multiply = erastofen(1, lst)
for i in list_multiply[::-1]:
    if number % i == 0:
        print('Самый большой простой делитель равен ', i)
        break