import random
sal = float(random.randint(1000, 1500))
if sal > 1250.0:
    salr = sal * 1.1
    print(f'seu salario era esse {sal}, mas a partir de agora vai ser esse abaixo:')
    print(f'Seu novo salário será de {salr:.2f}R$')
else:
    salr = sal * 1.15
    print(f'seu salario era esse {sal}, mas a partir de agora vai ser esse abaixo:')
    print(f'Seu novo salário será de {salr:.2f}R$')

