from random import randint
num = []
while len(num) != 11:
    n = randint(0,10)
    if n not in num:
        num.append(n)
print(sorted(num))