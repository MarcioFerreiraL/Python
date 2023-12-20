<<<<<<< HEAD
from random import randint
inferno = []
for c in range(0,10):
    boletim = []
    notas = []
    nome = f'Aluno{c+1}'
    for d in range(0, 4):
        nota = randint(0, 10)
        notas.append(nota)
    media = sum(notas) / len(notas)
    boletim.append(nome[:])
    boletim.append(media)
    inferno.append(boletim[:])
print('=' * 20)
print('MEDIAS DOS ALUNOS')
print('=' * 20)
for c in range(0,10):
    print(f'{inferno[c][0]:.<9}{inferno[c][1]:.>10}')
=======
from random import randint
inferno = []
for c in range(0,10):
    boletim = []
    notas = []
    nome = f'Aluno{c+1}'
    for d in range(0, 4):
        nota = randint(0, 10)
        notas.append(nota)
    media = sum(notas) / len(notas)
    boletim.append(nome[:])
    boletim.append(media)
    inferno.append(boletim[:])
print('=' * 20)
print('MEDIAS DOS ALUNOS')
print('=' * 20)
for c in range(0,10):
    print(f'{inferno[c][0]:.<9}{inferno[c][1]:.>10}')
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
print('=' * 20)