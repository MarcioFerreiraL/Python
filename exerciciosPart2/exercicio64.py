import random
num = x = 0
while num != 9:
    num = random.randint(1,10)
    x += num
print(f'A soma de todos os numero foi {x}')