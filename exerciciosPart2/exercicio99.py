<<<<<<< HEAD
from random import randint
def maior(* x):
    y = list()
    for c in x:
        y+=c
    print(max(y))
z = randint(5, 15)
numeros = []
for c in range(0, z):
    numeros.append(randint(1,100))
=======
from random import randint
def maior(* x):
    y = list()
    for c in x:
        y+=c
    print(max(y))
z = randint(5, 15)
numeros = []
for c in range(0, z):
    numeros.append(randint(1,100))
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
maior(numeros)