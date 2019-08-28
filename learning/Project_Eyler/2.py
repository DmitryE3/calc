"""Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10
элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


def fibonachi(list_fib):
    new_element = list_fib[-1] + list_fib[-2]
    list_fib.append(new_element)


list_fib = [1, 2]
while True:
    fibonachi(list_fib)
    if list_fib[-1] + list_fib[-2] > 4000000:
        break
print(sum(filter(lambda x: x % 2 == 0, list_fib)))
