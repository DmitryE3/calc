phrase = input('Введите предложение')
print('Вы ввели предложение: ', phrase)
words = phrase.split(' ')
max_word = ''
for word in words:
    if len(word) > len(max_word):
        max_word = word
print(max_word)
