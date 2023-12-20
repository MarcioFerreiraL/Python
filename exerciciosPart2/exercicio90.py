<<<<<<< HEAD
from random import randint

inferno = []

for c in range(0, 10):
    boletim = dict()
    media = 0
    situacao = ""
    notas = []
    nome = f'Aluno{c+1}'
    for d in range(0, 4):
        nota = randint(0, 10)
        notas.append(nota)
    media = sum(notas) / len(notas)
    if media < 4:
        situacao = 'Reprovado'
    elif 4 <= media < 6:
        situacao = 'Recuperação'
    elif media >= 6:
        situacao = 'Aprovado'
    boletim['nome'] = nome
    boletim['media'] = media
    boletim['situacao'] = situacao
    inferno.append(boletim)
print('NOME       MEDIA       SITUACAO')
for aluno in inferno:
    print(f"{aluno['nome']:<10} {aluno['media']:.2f} {aluno['situacao']:>15}")

=======
from random import randint

inferno = []

for c in range(0, 10):
    boletim = dict()
    media = 0
    situacao = ""
    notas = []
    nome = f'Aluno{c+1}'
    for d in range(0, 4):
        nota = randint(0, 10)
        notas.append(nota)
    media = sum(notas) / len(notas)
    if media < 4:
        situacao = 'Reprovado'
    elif 4 <= media < 6:
        situacao = 'Recuperação'
    elif media >= 6:
        situacao = 'Aprovado'
    boletim['nome'] = nome
    boletim['media'] = media
    boletim['situacao'] = situacao
    inferno.append(boletim)
print('NOME       MEDIA       SITUACAO')
for aluno in inferno:
    print(f"{aluno['nome']:<10} {aluno['media']:.2f} {aluno['situacao']:>15}")

>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
