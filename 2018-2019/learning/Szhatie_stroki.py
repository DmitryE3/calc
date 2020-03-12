"""
Строка a2b3c5 после разжатия становится строкой aabbbccccc. Сожмите данную вам строку S.
"""

stroka = 'aabbbccccc'
stroka = list(stroka)
compressed_str=''
last = None
for i in stroka:
    if i != last:
        last = i
        compressed_str = compressed_str + i + str(stroka.count(i))
print(compressed_str)
