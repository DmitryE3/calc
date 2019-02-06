#Дан cписок.Определить в нем наиболее встречаемое значение. Программа ниже ищет только  одно значение.Если в списке
#два значения встречаются с одинаковой частотой, то будет определено только одно из них.

import random

def make_list(size_list):
    lst=[random.randint(0,100) for _ in range(size_list)]
    return lst

def find_elm(lst):
    elm=None
    score=0
    print(lst)
    for i in lst:
        x=lst.count(i)
        if x>=score:
            score=x
            elm=i
    return score,elm

def main():
    size_list=int(input('Введите размер списка: '))
    score,elm=find_elm(make_list(size_list))
    print('Чаще всего встречается элемент ', elm, 'в колличестве ', score)

if __name__=='__main__':
    main()