def notas(* a):
    """
    Pega as notas que adicionar no parametro e retorna a quantidade de notas inseridas,
    a maior e menor nota e media das notas.
    """
    notasA = list()
    alunos = dict()
    for c in a:
        notasA += c
    alunos['Quantidade de notas'] = len(notasA)
    alunos['A maior nota'] = max(notasA)
    alunos['A menor nota'] = min(notasA)
    alunos['A média da turma'] = sum(notasA)/len(notasA)
    for pos, aluno in alunos.items():
        print(f'{pos} - {aluno:.1f}')
from random import randint
num = randint(1, 20)
nota = list()
for c in range(0, num):
    nota.append(randint(0, 10))
notas(nota)
help(notas)