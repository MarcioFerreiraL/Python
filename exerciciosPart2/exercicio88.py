<<<<<<< HEAD
from random import randint
megasena = []
x = int(input('Quantos jogos voce deseja? '))
for c in range(0, x):
    num = []
    for d in range(0, 6):
        n = randint(1, 60)
        num.append(n)
    megasena.append(num[:])
for c in range(0, x):
=======
from random import randint
megasena = []
x = int(input('Quantos jogos voce deseja? '))
for c in range(0, x):
    num = []
    for d in range(0, 6):
        n = randint(1, 60)
        num.append(n)
    megasena.append(num[:])
for c in range(0, x):
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print(f'{megasena[c]}', end='\n')