pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
x = 1
y = pt
while x != 11:
    y = r * x
    x += 1
    print(y)