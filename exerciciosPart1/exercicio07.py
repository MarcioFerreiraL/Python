nome = input('Nome do Aluno: ')
n1 = int(input('Digite a primeira nota de {} '.format(nome)))
n2 = int(input('Digite a segunda nota de {} '.format(nome)))
m = (n1 + n2) / 2
print('A média de {} é {}'.format(nome, m))