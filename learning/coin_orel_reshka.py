#Симуляция подбрасывания монеты
#Напишите программу, которая симулирует подбрасывание одной монеты столько раз, сколько захочет пользователь. Программа
#должна записывать результаты и подсчитывать сколько раз выпали орел и решка.

import random

def coin(orel,reshka):
    x=random.randint(0,1)
    if x==0:
        orel+=1
    else:
        reshka+=1
    return orel,reshka

def main():
    n=int(input("Введите число подбрасываний"))
    print("было произведено ",n," подбрасываний")
    orel,reshka=[0,0]
    while n!=0:
        n-=1
        orel,reshka=coin(orel,reshka)
    print("Орел выпал ",orel," раз")
    print("Решка выпала ", reshka, " раз")

if __name__=="__main__":
    main()
