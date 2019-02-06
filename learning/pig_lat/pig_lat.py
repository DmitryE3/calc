#Поросячья латынь
#Это «тайный язык», представляющий собой зашифрованный английский.
#Чтобы сделать поросяче-латинское слово из английского, нужно первые согласные
#звуки в слове переместить в конец и прибавить ay (Например: «banana»
#превращается в anana-bay). Подробнее о правилах читайте в Википедии

def make_pig_lat(word):
    punctuation_mark=""
    if word[len(word)-1] in ".,:!?":
        punctuation_mark=word[len(word)-1]
        word=word[:len(word)-1]
    if word[0] not in "aeiouy":
        for i in range(len(word)):
            if word[i] in "aeiouy":
                word=word[i:]+word[:i]+"ay"+punctuation_mark
                break
    else:
        word=word+"ay"+punctuation_mark
    return word

def main():
    words=str(input("Введите ваше предложение на английском языке: ")).lower()
    words=words.split(" ")
    for i in words:
        print(pig_lat(i))
    ext=input("\nPress Entr to exit")

if __name__=="__main__":
    main()
