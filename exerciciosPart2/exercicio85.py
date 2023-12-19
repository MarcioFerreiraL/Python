from random import randint
lista = []
p = []
i = []
for c in range(0, 10):
    num = randint(0, 20)
    if num % 2 == 0:
        p.append(num)
        lista.append(num)
    else:
        i.append(num)
        lista.append(num)
    lista.clear()
lista.append(p[:])
lista.append(i[:])
print(sorted(lista[0]))
print(sorted(lista[1]))