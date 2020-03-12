"""Последовательность Фибоначчи
Введите число, и программа сгенерирует последовательность Фибоначчи до этого
числа или до N-го числа
"""


def fibonachi(list_fib, n):
    if n == 1:
        #       return list_fib
        pass
    else:
        while True:
            x = list_fib[len(list_fib) - 1] + list_fib[len(list_fib) - 2]
            if x > n:
                break
            else:
                list_fib.append(x)
                fibonachi(list_fib, n)
    return list_fib


def main():
    list_fib = [0, 1]
    n = int(input('Введите число: '))
    print(fibonachi(list_fib, n))
    ext = input('Нажмите ENTR для выхода')


if __name__ == '__main__':
    main()
