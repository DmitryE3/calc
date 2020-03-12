"""Гипотеза Коллатца
Найдите число шагов, за которые получится единица, используя следующий процесс:
берём любое натуральное число n больше единицы. Если оно чётное, то делим его
на 2, а если нечётное, то умножаем на 3 и прибавляем 1
"""


def gipoteza_kollatza(n):
    count = 0  # Счетчик шагов
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    return count


def main():
    while True:
        n = int(input('Введите число, больше 1: '))
        if n > 1:
            break
    print(gipoteza_kollatza(n), ' шагов до единицы')
    ext = input("\nPress Entr to exit")


if __name__ == '__main__':
    main()
