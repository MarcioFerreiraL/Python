import random
num1 = random.randint(0,5)
num2 = int(input('Advinhe o numero que o computador escolheu (0 a 5) '))
if num1 == num2:
    print('Você acertou! PARABENS!')
else:
    print('Você errou :(')
    print('O numero correto era: ', num1)