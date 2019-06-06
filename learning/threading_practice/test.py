#последовательнсоть фибонначи

def fibon(sequence):
    x=sequence[-1]+sequence[-2]
    sequence.append(x)
    return sequence

sequence=[1,1]
number=int(input('Введите число: '))
while number>=sequence[-1]:
    fibon(sequence)
    print(sequence)
print(sequence[:-1])