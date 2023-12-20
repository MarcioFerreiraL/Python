<<<<<<< HEAD
from random import randint
from operator import itemgetter
jogo = {}
jogador = {}
for c in range(0, 4):
    numero = randint(1, 6)
    nome = f'Jogador{c + 1}'
    jogador[nome] = numero
    jogo = jogador
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'O vencedor é o {ranking[0][0]} que jogou {ranking[0][1]}')
=======
from random import randint
from operator import itemgetter
jogo = {}
jogador = {}
for c in range(0, 4):
    numero = randint(1, 6)
    nome = f'Jogador{c + 1}'
    jogador[nome] = numero
    jogo = jogador
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'O vencedor é o {ranking[0][0]} que jogou {ranking[0][1]}')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
