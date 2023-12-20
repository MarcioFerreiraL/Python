from random import randint
def funcao(a, b, c):
    if a > b:
        c = -c
    for d in range(a, b+1, c):
        print(d, end=' ')
x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))
z = int(input('Digite um numero: '))
funcao(x, y, z)