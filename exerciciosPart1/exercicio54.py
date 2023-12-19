import random
an = 0; idade = 0; p = 0
for c in range(0, 7):
    an = random.randint(1995, 2013)
    idade = 2023 - an
    print(f'{idade}')
    if idade >= 18:
        p += 1
print(f'{p} pessoas são maiores de idade!')

