import random
num1 = random.randint(0,10)
num2 = random.randint(0, 10)
jogos = 0
print('-' * 50)
while num1 != num2:
    print(f'Computador1 jogou {num1} e o Computador jogou {num2}')
    print('-' * 50)
    jogos += 1
    num1 = random.randint(0, 5)
    num2 = random.randint(0, 5)
print(f'Os computadores jogaram um total de {jogos} jogos para empatarem')