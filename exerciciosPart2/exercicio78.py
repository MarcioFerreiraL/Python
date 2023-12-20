from random import randint
num = []
for c in range(0, 10):
    n = randint(0,100)
    num.append(n)
print(f'o menor numero da lista é {min(num)} e está na posição {num.index(min(num))}')
print(f'o maior numero da lista é {max(num)} e está na posição {num.index(max(num))}')
print(num)