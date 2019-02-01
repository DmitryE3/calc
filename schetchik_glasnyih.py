"""
Счетчик гласных
Вводится строка, и программа считает количество гласных в тексте.
Для усложнения задачи можно генерировать отчет о том, сколько раз какая
гласная была найдена.
"""
def vowel_counter(words): #Счетчик всех гласных
    count=0
    for i in words:
        if i in 'aeiou':
            count+=1
    return count

def sum_different_vowel(words): #Подсчет гласных поштучно
    for i in 'aeiou':
        print('букв ', i,' в строке', words.count(i), 'штук')

def main():
    words=str(input('Введите вашу строку: ')).lower()
    print(vowel_counter(words))
    sum_different_vowel(words)
    input('нажмите ентр чтоб выйти')

if __name__=='__main__':
    main()
