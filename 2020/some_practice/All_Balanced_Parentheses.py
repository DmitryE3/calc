"""

Write a function that makes a list of strings
representing all the ways you can balance n pairs of parentheses.
"""

import itertools

    
def get_variants(n):
    variants_list = list(set(itertools.permutations('()'*n, n*2)))
    for i in variants_list:
        counter = 0
        for j in i:
            if j=='(':
                counter +=1
            else:
                counter -=1
                if counter < 0:
                    variants_list.remove(i)
                    break
        else:
            print(''.join(i))


if __name__ == '__main__':
    x = int(input('Enter number - '))
    get_variants(x)

