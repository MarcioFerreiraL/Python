from random import randint
system = []
leves = []
pesadas = []
for c in range(0, 10):
    P = randint(60, 120)
    N = (f'Doide{c + 1}')
    PP = []
    PP.append(N)
    PP.append(P)
    system.append(PP[:])
    PP.clear()
print(f'{len(system)}')
for c in range(0, 10):
    M = (system[c][1])
    if M >= 100:
        pesadas.append(system[c][0])
    elif M <= 80:
        leves.append(system[c][0])
print(pesadas)
print(leves)
print(system)