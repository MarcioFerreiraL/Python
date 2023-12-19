pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
x = int(input('Quantos termos voce quer? ')) + 1
y = pt
c = 0
if x == 0:
    print('error')
else:
    while x != 0:
        y = r * c
        c += 1
        x -= 1
        print(y)