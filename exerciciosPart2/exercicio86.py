<<<<<<< HEAD
from random import randint
matriz = []
for c in range(0, 3):
    n = []
    for d in range(0, 3):
        num = randint(0, 50)
        n.append(num)
    matriz.append(n[:])
print('=' * 20)
for c in range(0, 3):
    if c != 0:
        print('')
    for d in range(0, 3):
        print(f'{matriz[c][d]:5}', end="")
    print('')
=======
from random import randint
matriz = []
for c in range(0, 3):
    n = []
    for d in range(0, 3):
        num = randint(0, 50)
        n.append(num)
    matriz.append(n[:])
print('=' * 20)
for c in range(0, 3):
    if c != 0:
        print('')
    for d in range(0, 3):
        print(f'{matriz[c][d]:5}', end="")
    print('')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print('=' * 20)