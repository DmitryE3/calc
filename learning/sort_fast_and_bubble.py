"""
Сортировка быстрая
"""
import random

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        x = random.choice(lst)
        left = [i for i in lst if i < x]
        centr = [x]*lst.count(x)
        right = [i for i in lst if i > x]
        return quick_sort(left) + centr + quick_sort(right)
print(quick_sort([1,2,5,3,7,1,3,2,85]))

def buble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1,i,-1):
            if lst[j] < lst[j-1]:
                lst[j],lst[j-1] = lst[j-1], lst[j]
    return lst

print(buble_sort([1,2,5,3,7,1,3,2,85]))