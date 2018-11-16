#Поросячья латынь
#Это «тайный язык», представляющий собой зашифрованный английский.
#Чтобы сделать поросяче-латинское слово из английского, нужно первые согласные
#звуки в слове переместить в конец и прибавить ay (Например: «banana»
#превращается в anana-bay). Подробнее о правилах читайте в Википедии

def pig_lat(word):
    if word[0] not in "aeiouy":
        for i in range(len(word)):
            if word[i] in "aeiouy":
                word=word[i:]+word[:i]+'ay'
                break
    else:
        word=word+'ay'
    print(word,end=' ')

def main():
    words=str(input('введите ваше предложение на английском языке: ')).lower()
    words=words.split(' ')
    for i in words:
        pig_lat(i)
    ext=input('\nPress Entr to exit')

if __name__=='__main__':
    main()
