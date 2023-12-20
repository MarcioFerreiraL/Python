from random import randint
def area(a, b):
    v = a * b
    print(f'{a} por {b} é igual a {v}')

x = randint(1, 100)
y = randint(1, 100)
area(x, y)