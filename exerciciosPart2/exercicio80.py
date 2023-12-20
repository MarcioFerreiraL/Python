<<<<<<< HEAD
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
=======
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
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print(num)