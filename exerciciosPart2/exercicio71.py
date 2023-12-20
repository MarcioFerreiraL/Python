<<<<<<< HEAD
import random
valorI = valor = random.randint(1, 10000)
cinquenta = vinte = dez = um = 0
while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    else:
        break

print(f'Foram usadas {cinquenta} cedulas de 50R$, {vinte} cedulas de 20R$')
print(f'{dez} cedulas de 10R$, {um} cedulas de 1R$')
=======
import random
valorI = valor = random.randint(1, 10000)
cinquenta = vinte = dez = um = 0
while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    else:
        break

print(f'Foram usadas {cinquenta} cedulas de 50R$, {vinte} cedulas de 20R$')
print(f'{dez} cedulas de 10R$, {um} cedulas de 1R$')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print(f'Para um valor de: {valorI}R$')