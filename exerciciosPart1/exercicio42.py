import random
lado1 = random.randint(0, 10)
lado2 = random.randint(0, 10)
lado3 = random.randint(0, 10)
print('{} < {} + {}'.format(lado1, lado2, lado3))

if lado1 < lado2 + lado3:
    print('Esse triagulo existe!')
    if lado1 == lado2 == lado3:
        print('Esse triângulo é EQUILATERO')
    elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('Esse triângulo é ISOCELES')
    elif lado1 != lado2 != lado3:
        print('Esse triângulo é ESCALENO')
else:
    print('Esse triangulo não existe')