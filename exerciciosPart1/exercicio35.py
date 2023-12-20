import random
lado1 = random.uniform(0, 100)
lado2 = random.uniform(0, 100)
lado3 = random.uniform(0, 100)
print('{:.2f} < {:.2f} + {:.2f}'.format(lado1, lado2, lado3))
if lado1 < lado3 + lado2:
    print('\033[34mEsse triângulo existe!')
else:
    print('\033[32mEsse triângulo não existe :(')