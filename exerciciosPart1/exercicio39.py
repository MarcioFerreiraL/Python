import random
ano = random.randint(2003, 2008)
idade = 2023 - ano
if idade == 18:
    print(f'Voce tem {idade} anos e ja esta na hora de se alistar!')
elif idade > 18:
    tempo = idade - 18
    print(f'Voce tem {idade} anos e ja passou {tempo} ano que voce devia ter se alistado')
elif idade < 18:
    tempo = 18 - idade
    print(f'Voce tem {idade} anos e ainda falta {tempo} anos para poder se alistar')