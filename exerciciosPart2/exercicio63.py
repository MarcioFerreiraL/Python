import random
x = numA = num = 0
y = 1
while x != 7:
    x += 1
    num = y + numA
    print(numA)
    numA = y
    y = num
