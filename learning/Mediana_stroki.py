"""
У нас есть список целых чисел. Найдите в нём медиану. Реализуйте функцию, которая добавляет новый элемент к этому
списку, при этом считаю новую медиану.
"""
spisok = [5,2,18,8]


def add_and_find(spisok):
    spisok.append(int(input('Введите число: ')))
    spisok.sort()
    print(spisok)
    if len(spisok) % 2 != 0:
        med = spisok[int(len(spisok)/2)]
    else:
        med = (spisok[int(len(spisok)/2)] + spisok[int(len(spisok)/2) - 1])/2
    return med


print(add_and_find(spisok))