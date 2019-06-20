"""Решето Эратосфена
Решето Эратосфена — один из самых эффективных способов нахождения всех
небольших простых чисел (ниже 10 миллионов)
"""


def erastofen(count, x):
    for i in x:
        if i != x[count] and i % x[count] == 0:
            x.remove(i)
    try:
        erastofen(count + 1, x)
    except:
        print(x)


def mnozhestvo(number):
    x = []
    for i in range(1, number):
        x.append(i)
    return x


def main():
    try:
        number = int(input('Введите число больше 1: '))
        x = mnozhestvo(number)
        count = 1
        erastofen(count, x)
    except ValueError:
        print('Введите тольо целое число больше 1')
        main()


if __name__ == '__main__':
    main()
    ext = input("\nPress Entr to exit")
