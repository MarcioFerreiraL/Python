from random import randint, choice
def dividirtela():
    print('-' * 50)
gerenciamento = []
mulheres = []
for c in range(0, 10): # Registrar dados
    aproveitamento = dict()
    nome = f'Pessoa{c+1}'
    sex = choice(['Masculino', 'Feminino'])
    an = randint(1990, 2010)
    idade = 2023 - an
    aproveitamento['nome'] = nome
    aproveitamento['sexo'] = sex
    aproveitamento['idade'] = idade
    gerenciamento.append(aproveitamento) # Cria uma lista de todas as informações de uma pessoa
idades = [pessoa['idade'] for pessoa in gerenciamento]
media = sum(idades) / len(idades) # Cálculo da média de idades corretamente fora do loop
mulheres = [pessoa for pessoa in gerenciamento if pessoa['sexo'] == 'Feminino'] # Criar lista de mulheres
acima_media = [pessoa for pessoa in gerenciamento if pessoa['idade'] > media] # Pessoas com idade acima da média
dividirtela()
print(f'Foram cadastrados um total de {len(gerenciamento)}')
dividirtela()
print('LISTA DAS MULHERES')
dividirtela()
for pessoa in mulheres:
    print(f'Nome: {pessoa["nome"]}')
    print(f'Sexo: {pessoa["sexo"]}')
    print(f'Idade: {pessoa["idade"]}')
dividirtela()
print(f'A média de idade do grupo é: {media:.2f}')
dividirtela()
print('PESSOAS COM IDADE ACIMA DA MEDIA')
dividirtela()
for pessoa in acima_media:
    print(f'Nome: {pessoa["nome"]}')
    print(f'Sexo: {pessoa["sexo"]}')
    print(f'Idade: {pessoa["idade"]}')
dividirtela()