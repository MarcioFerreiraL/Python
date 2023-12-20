<<<<<<< HEAD
from random import randint
num = []
while len(num) != 11:
    n = randint(0,10)
    if n not in num:
        num.append(n)
print(f'Foi digitado {len(num)} vezes')
print('Lista no modo reverso: ')
print(sorted(num, reverse=True))
if 5 in num:
    print('5 está na lista.')
else:
=======
from random import randint
num = []
while len(num) != 11:
    n = randint(0,10)
    if n not in num:
        num.append(n)
print(f'Foi digitado {len(num)} vezes')
print('Lista no modo reverso: ')
print(sorted(num, reverse=True))
if 5 in num:
    print('5 está na lista.')
else:
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print('5 não esta na lista.')