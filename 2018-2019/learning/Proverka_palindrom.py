"""Проверка на палиндром
Программа проверяет на то, что введенная строка является палиндромом
(то есть читается слева направо так же, как и справа налево)
"""


def revers_word(word):
    return word[::-1]


def main():
    word = str(input('Введите слово на проверку полиндрома: ')).lower()
    if word == revers_word(word):
        print('Это слово полиндром')
    else:
        print('Это не полиндром')
    input('press entr to exit')


if __name__ == '__main__':
    main()
