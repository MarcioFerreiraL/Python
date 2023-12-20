<<<<<<< HEAD
from random import randint
num = []
while len(num) != 11:
    n = randint(0,10)
    if n not in num:
        num.append(n)
=======
from random import randint
num = []
while len(num) != 11:
    n = randint(0,10)
    if n not in num:
        num.append(n)
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print(sorted(num))