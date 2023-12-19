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
    print(f'{megasena[c]}', end='\n')