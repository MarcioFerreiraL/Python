def voto(an):
    idade = 2023 - an
    if idade >= 18:
        return 'OBRIGATORIO'
    elif 16 <= idade < 18 or idade > 60:
        return 'OPCIONAL'
    else:
        return 'NEGADO'
from random import randint
titulo = voto(randint(1945, 2015))
print(titulo)