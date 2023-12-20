from random import randint
num = []
while len(num) != 5:
    n = randint(0, 10)
    c = 0
    if c == 0:
        num.append(n)
    if num[c] < n:
        num.insert(c, n)
    c += 1
print(num)