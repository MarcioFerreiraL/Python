import random
lista = []
while True:
    num = random.randint(1, 50)
    lista.append(num)
    if num == 9:
        break
print(f'Foram digitados {len(lista)} numeros')
print(f'A soma de todos os numeros é {sum(lista)}')