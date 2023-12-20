<<<<<<< HEAD
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
=======
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
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
sumPar(numeros)