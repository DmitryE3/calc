"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""

prostoi_list = []
x = 1
while len(prostoi_list) != 10001:
    x += 1
    for i in range(2, int(x/2)+1):
        if x%i == 0:
            break
    else:
        prostoi_list.append(x)
print(prostoi_list[-1], len(prostoi_list))



