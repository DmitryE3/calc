"""Дана матрица целых чисел. Вводится число. Выяснить, какие строки и столбцы матрицы содержат данное число."""
import random


def matrix_create(n, m):  # n-число строк m-число столбцов
    matrix = []
    k = 0
    while k != n:
        k += 1
        string = []
        for i in range(m):
            string.append(random.randint(0, 100))
        matrix.append(string)
    return matrix


def find_number(x, matrix):
    spisok = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if x == matrix[i][j]:
                spisok.append([i, j])  # i - string; j - column
    return spisok


def main():
    n = int(input('Введите число строк матрицы: '))
    m = int(input('Введите число столбцов: '))
    x = int(input('Введите искомое число от 0 до 100: '))
    spisok = find_number(x, matrix_create(n, m))
    if len(spisok) > 0:
        for i in spisok:
            print('строка ' + str(i[0]) + ' столбец ' + str(i[1]))
    else:
        print('Такого числа нет в матрице')


if __name__ == '__main__':
    main()
