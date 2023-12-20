from random import randint
from random import choice
nomes = ['Maria', 'Marcio', 'Pedro', 'Livia', 'Marcos', 'Moyses', 'Ranaa', 'Rapariga']
cadastro = dict()
nome = choice(nomes)
an = randint(1970, 2005)
idade = 2023 - an
ctps = randint(0, 1)
if ctps != 0:
    ac = an + 18
    salario = randint(1000, 5000)
    aposentar = ((ac + 35) - an)
    cadastro['nome'] = nome
    cadastro['idade'] = idade
    cadastro['ctps'] = ctps
    cadastro['ano de contratação'] = ac
    cadastro['salario'] = salario
    cadastro['aposentar'] = aposentar
else:
    cadastro['nome'] = nome
    cadastro['idade'] = idade
    cadastro['ctps'] = ctps
for c, d in cadastro.items():
    print(f'{c.upper():.<20}{d:.>10}')
