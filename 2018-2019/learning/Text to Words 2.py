"""Доработка задачи из Text_to_words до возможности выбора нужного текстового файла"""

import Text_to_words


def main():
    file_name = input("Введите имя файла(или путь к файлу, если он в другой папке): ")
    with open(file_name, 'r', encoding='utf-8') as file:
        text = Text_to_words.delete_punctuation(file.read())
        print(Text_to_words.converter_text_to_words(text))


if __name__ == '__main__':
    main()
