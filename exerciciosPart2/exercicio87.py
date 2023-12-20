<<<<<<< HEAD
from random import randint
matriz = []
soma = 0
soma3 = 0
maior = 0
for c in range(0, 3):
    n = []
    for d in range(0, 3):
        num = randint(0, 50)
        n.append(num)
        if num % 2 == 0:
            soma += num
        if d == 2:
            soma3 += num
        if c == 1:
            maior = max(n)
    matriz.append(n[:])
print('=' * 20)
for c in range(0, 3):
    if c != 0:
        print('')
    for d in range(0, 3):
        print(f'{matriz[c][d]:5}', end="")
    print('')
print('=' * 20)
print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
=======
from random import randint
matriz = []
soma = 0
soma3 = 0
maior = 0
for c in range(0, 3):
    n = []
    for d in range(0, 3):
        num = randint(0, 50)
        n.append(num)
        if num % 2 == 0:
            soma += num
        if d == 2:
            soma3 += num
        if c == 1:
            maior = max(n)
    matriz.append(n[:])
print('=' * 20)
for c in range(0, 3):
    if c != 0:
        print('')
    for d in range(0, 3):
        print(f'{matriz[c][d]:5}', end="")
    print('')
print('=' * 20)
print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print(f'O maior valor da segunda linha é: {maior}')