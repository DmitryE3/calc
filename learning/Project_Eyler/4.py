""" Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""
def ispalindrome(x):
    if str(x) == str(x)[::-1]:
        return True


palindrome_list = []
for i in range(100,1000):
    for j in range (i,1000):
        x = i * j
        if ispalindrome(x):
            palindrome_list.append(x)
print(max(palindrome_list))