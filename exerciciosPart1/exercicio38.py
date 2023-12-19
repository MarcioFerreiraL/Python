import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
if num1 > num2:
    print(f'o {num1} é maior que o {num2}')
elif num2 > num1:
    print(f'o {num2} é maior que o {num1}')
elif num2 == num1:
    print(f'o numeros {num1} e {num2} são iguais')
else:
    print('algo de errado nao está certo')