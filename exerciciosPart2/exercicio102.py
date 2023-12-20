def fatoriar(num, logico):
    a = 1
    if logico == 'S':
        for c in range(num, 0, -1):
            a *= c
            if c == 1:
                print(f'{c} ', end='')
            else:
                print(f'{c} x', end=' ')
        print(f'= {a}')
    elif logico == 'N':
        from math import factorial
        print(factorial(num))
    else:
        return False
from random import randint, choice
logico = ['S', 'N']
doido = fatoriar(randint(0, 10), choice(logico))
if doido == False:
    print('Escreva S/N!')
