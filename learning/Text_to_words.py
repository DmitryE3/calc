""""Вводится нормализованный текст, который кроме слов может содержать определенные
знаки препинания. Программа строит список слов, знаки препинания исключаются.
"""


def delete_punctuation_not_right(text_list):  # данный вариант проще, но не рассчитан на такие знаки как !!! или !?
    new_text = []
    punctuation_marks = '.,:;!/?()#"@*^'
    for i in text_list:
        if i[0] in punctuation_marks:
            i = i[1:]
        if i[-1] in punctuation_marks:
            i = i[:-1]
        new_text.append(i)
    return new_text


def delete_punctuation(text):
    new_text = ''
    punctuation_marks = '.,:;!/?()#"@*^'
    for i in text:
        if i not in punctuation_marks:
            new_text += i
    return new_text


def converter_text_to_words(text):
    return text.split()


def main():
    text = input('Введите ваш текст: ')
    print(converter_text_to_words(delete_punctuation(text)))


if __name__ == "__main__":
    main()
