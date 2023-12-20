<<<<<<< HEAD
import random
lista = []
while True:
    num = random.randint(1, 50)
    lista.append(num)
    if num == 9:
        break
print(f'Foram digitados {len(lista)} numeros')
=======
import random
lista = []
while True:
    num = random.randint(1, 50)
    lista.append(num)
    if num == 9:
        break
print(f'Foram digitados {len(lista)} numeros')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print(f'A soma de todos os numeros é {sum(lista)}')