<<<<<<< HEAD
from random import randint
gerenciamento = []
x = int(input('Quantos jogadores voce quer ver? '))
for c in range(0, x):
    nump = randint(0, 40)
    gols = [randint(0, 3) for _ in range(nump)]
    aproveitamento = {
        'nome': f'Jogador{c+1}',
        'numeros de partidas': nump,
        'gols': sum(gols)
    }
    gerenciamento.append(aproveitamento)
print("-" * 25)
for jogador in gerenciamento:
    print(f"Nome: {jogador['nome']}")
    print(f"Número de partidas: {jogador['numeros de partidas']}")
    print(f"Gols: {jogador['gols']}")
=======
from random import randint
gerenciamento = []
x = int(input('Quantos jogadores voce quer ver? '))
for c in range(0, x):
    nump = randint(0, 40)
    gols = [randint(0, 3) for _ in range(nump)]
    aproveitamento = {
        'nome': f'Jogador{c+1}',
        'numeros de partidas': nump,
        'gols': sum(gols)
    }
    gerenciamento.append(aproveitamento)
print("-" * 25)
for jogador in gerenciamento:
    print(f"Nome: {jogador['nome']}")
    print(f"Número de partidas: {jogador['numeros de partidas']}")
    print(f"Gols: {jogador['gols']}")
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print("-" * 25)