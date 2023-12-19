import random
num = random.randint(0, 100)
if num % 2 == 1:
    print('O numero {} é impar'.format(num))
else:
    print('O numero {} é par'.format(num))