#Найдите число шагов, за которые получится единица, используя следующий процесс:
#берём любое натуральное число n больше единицы. Если оно чётное, то делим его
#на 2, а если нечётное, то умножаем на 3 и прибавляем 1
n=int(input('Введите число, больше 1'))
count=0
while n!=1:
    count+=1
    if n%2==0:
        n=n/2
    else:
        n=n*3+1
print(k,' шагов до единицы')
