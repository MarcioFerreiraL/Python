pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
f = ((pt + 1) * 10) * r + 1
for c in range(pt, f, r):
    print(c)