#В Волшебной стране используются монетки достоинством A1, A2,..., AM. Волшебный человечек пришел в магазин и обнаружил,
#что у него есть ровно по две монетки каждого достоинства. Ему нужно заплатить сумму N. Напишите программу, определяющую,
#сможет ли он расплатиться без сдачи.
#Входные данные
#На вход программы  сначала поступает число N (1 <= N <= 10^9), затем - число M (1 <= M <= 15) и далее M попарно
#различных чисел A1, A2,..., AM (1 <= Ai <= 10^9).
#Выходные данные
#Сначала выведите K - количество монет, которое придется отдать Волшебному человечку, если он сможет заплатить указанную
#сумму без сдачи. Далее выведите K чисел, задающих достоинства монет. Если решений несколько, выведите вариант,
#в котором Волшебный человек отдаст наименьшее возможное количество монет. Если таких вариантов несколько, выведите
#любой из них.
#Если без сдачи не обойтись, то выведите одно число 0. Если же у Волшебного человечка не хватит денег, чтобы заплатить
#указанную сумму, выведите одно число -1 (минус один).
import itertools


#def combinations(money):                          #Вариант с перебором всех возможных вариантов
#    all_combination = []
#    for i in range(len(money)+1):
#        for j in itertools.combinations(money,i):
#            all_combination.append(j)
#    return all_combination

#def find_change(all_combination,N):
#    for i in all_combination[1:]:
#        if sum(i)%N==0:
#            print(len(i),i)
#            break
#    else:
#        print(0)

def get_variants(money):                               # Вариант, в котором программа ищет первый подходящий вариант
    for i in range(1,len(money)+1):
        for j in itertools.combinations(money,i):
            yield j

def try_sum(money,N):
    if sum(money)<N:
        print(-1)
    else:
#        find_change(all_combination,N)
        temp=get_variants(money)
        while True:
            try:
                x=next(temp)
                if sum(x)%N==0:
                    print(len(x),x)
                    break
            except:
                print(0)
                break

def get_coins(x):
    x=[int(i) for i in x.split()]
    money=x+x
    return money

def main():
    N=112
    M='11 20 30 40 11 99 5'
    try_sum(get_coins(M),N)

if __name__=='__main__':
    main()