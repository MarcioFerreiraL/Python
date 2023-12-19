import random
num = random.randint(3,100)
p = 0
for c in range(num - 1, 2, -1):
    if (num % c == 0):
        p += 1
if p > 0:
    print(f'O numero {num} não é primo!')
elif p == 0:
    print(f'O numero {num} é primo!')
else:
    print('error')