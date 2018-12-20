#Вводится нормализованный текст, который кроме слов может содержать определенные
#знаки препинания. Программа строит список слов, знаки препинания исключаются.

def delete_punctuation(text):
    new_text=''
    punctuation_marks='.,:;!/?()#"@*^'
    for i in text:
        if i not in punctuation_marks:
            new_text+=i
    return new_text

def converter_text_to_word(text):
    return text.split()

text=input('Введите ваш текст: ')
text=converter_text_to_word(delete_punctuation(text))
print(text)
