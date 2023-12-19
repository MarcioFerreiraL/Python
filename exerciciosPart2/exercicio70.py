import random
p = preco = b = 0
nomeP = ['Carro', 'Celular', 'Brinquedo', 'Cama', 'Fone', 'Televisão', 'Mouse', 'Teclado', 'Caneta', 'Camisinha', 'Perfume']
C = 'S'
gasto = [3000]
while True:
    if C == 'N':
        break
    elif C == 'S':

        preco = random.uniform(50, 2050)
        nome = random.choice(nomeP)
        print('-' * 20)
        print(f'nome: {nome}')
        print(f'preço: {preco:.2f}R$')
        print('-' * 20)

        if preco > 1000:
            p += 1

        if min(gasto) > preco:
            b = nome
        gasto.remove(3000)
        gasto.append(preco)

    else:
        print('\033[2merror')
    C = input('Quer continuar? [S/N] ').upper().strip()[0]

print('\033[1;33mEsse foi o resultado da pesquisa:')
print(f'\033[34mForam gastos um total de: {sum(gasto):.2f}R$.')
print(f'\033[35m{p} produtos custam mais de 1000R$.')
print(f'\033[36m{b} é o item mais barato da lista.')