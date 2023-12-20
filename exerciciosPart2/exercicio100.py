from random import randint
def sorteio(x):
    for c in range(0, 5):
        y = randint(0, 100)
        x.append(y)
    print(x)
def sumPar(x):
    y = []
    for c in x:
       if c % 2 == 0:
           y.append(c)
    print(f'Essa é a soma de todos os numeros pares: {sum(y)}')
numeros = []
sorteio(numeros)
sumPar(numeros)