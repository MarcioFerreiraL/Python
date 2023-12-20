<<<<<<< HEAD
import random
nt = ()
for c in range(0, 10):
    e = random.randint(1, 10)
    nt += (e,)
print(nt)
print(f'O número 9 apareceu {nt.count(9)} vezes')
if 3 in nt:
    print(f'O número 3 apareceu na posição {nt.index(3)}')
else:
    print(f'O elemento 3 não está presente na tupla.')

np = tuple(x for x in nt if x % 2 == 0)
print(f'Os números pares são: {np}')
=======
import random
nt = ()
for c in range(0, 10):
    e = random.randint(1, 10)
    nt += (e,)
print(nt)
print(f'O número 9 apareceu {nt.count(9)} vezes')
if 3 in nt:
    print(f'O número 3 apareceu na posição {nt.index(3)}')
else:
    print(f'O elemento 3 não está presente na tupla.')

np = tuple(x for x in nt if x % 2 == 0)
print(f'Os números pares são: {np}')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
