<<<<<<< HEAD
from random import randint
gerenciamento = []
for c in range(0, 3):
    aproveitamento = dict()
    gols = []
    nome = (f'Jogador{c+1}')
    nump = randint(0, 40)
    for d in range(0, nump):
        gols.append(randint(0, 5))
    golsf = (sum(gols))
    aproveitamento['nome'] = nome
    aproveitamento['numeros de partidas'] = nump
    aproveitamento['gols'] = golsf
    gerenciamento.append(aproveitamento)
for jogador in gerenciamento:
    print(f"Nome: {jogador['nome']}")
    print(f"Número de partidas: {jogador['numeros de partidas']}")
    print(f"Gols: {jogador['gols']}")
=======
from random import randint
gerenciamento = []
for c in range(0, 3):
    aproveitamento = dict()
    gols = []
    nome = (f'Jogador{c+1}')
    nump = randint(0, 40)
    for d in range(0, nump):
        gols.append(randint(0, 5))
    golsf = (sum(gols))
    aproveitamento['nome'] = nome
    aproveitamento['numeros de partidas'] = nump
    aproveitamento['gols'] = golsf
    gerenciamento.append(aproveitamento)
for jogador in gerenciamento:
    print(f"Nome: {jogador['nome']}")
    print(f"Número de partidas: {jogador['numeros de partidas']}")
    print(f"Gols: {jogador['gols']}")
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print("-" * 25)