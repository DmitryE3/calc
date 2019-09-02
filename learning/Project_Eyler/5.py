""" 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""
import time

time_start = time.time()
x = 2520
while True:
    x += 1
    for i in range(2, 21):
        if x % i != 0:
            break
    else:
        print(x)
        time_end = time.time() - time_start
        break
print(time_end)

