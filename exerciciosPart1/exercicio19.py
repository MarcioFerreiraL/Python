from random import choice
nome1 = input('Digite o nome de um aluno ')
nome2 = input('Digite o nome de um aluno ')
nome3 = input('Digite o nome de um aluno ')
nome4 = input('Digite o nome de um aluno ')
e = [nome1, nome2, nome3, nome4]
print('O aluno escolhido foi o {}'. format(random.choice(e)))