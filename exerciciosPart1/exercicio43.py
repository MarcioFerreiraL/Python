import random
peso = random.uniform(40, 150)
altura = random.uniform(1.5, 2.2)
imc = peso / pow(altura, 2)
if imc < 18.5:
    print(f'Abaixo do peso! imc - {imc:.2f}')
elif 18.5 <= imc < 25:
    print(f'Peso ideal! imc - {imc:.2f}')
elif 25 <= imc < 30:
    print(f'Sobrepeso! imc - {imc:.2f}')
elif 30 <= imc < 40:
    print(f'Obesidade! imc - {imc:.2f}')
elif 40 >= imc:
    print(f'Obesidade morbida! imc - {imc:.2f}')