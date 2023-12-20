import random
s = 0; p = 0
for c in range(0, 6):
    p = int(input('Digite um numero: '))
    if p % 2 == 0:
        s += p
print(f'A soma de todos os numeros pares que foi digitado é {s}')