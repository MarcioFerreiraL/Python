from random import randint
num = []
pares = []
impares = []
for d in range(0, 20):
    n = randint(0,100)
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Lista de números:", num)
print("Números pares:", pares)
print("Números ímpares:", impares)
