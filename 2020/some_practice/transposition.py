"""
Вы должны сделать все возможные перестановки входной строки и удалить дубликаты, если они есть.
 Это означает, что вы должны перетасовать все буквы из ввода во всех возможных порядках.

You must do all possible permutations of the input string and remove duplicates, if any.
This means that you must shuffle all the letters from the input in all possible orders.
"""
import itertools


def permutation(string):
    data = list(itertools.combinations_with_replacement(string, len(string)))
    return data

def main():
    temp = set(permutation(input('Enter your string: ')))
    print(temp)
    for i in temp:
        print(''.join(i))


if __name__ == '__main__':
    main()