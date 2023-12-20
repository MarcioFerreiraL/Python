import random
somaidade = 0
nome = ["Marcio", "Moyses", "Ana", "Livia"]
idade = 0; idadeM : int = 0; fem20 = 0
sexo = ['Masc', 'Fem']
for c in range(0, 4):
    nomet = str(random.choice(nome))
    idade = random.randint(1, 100)
    sexot = str(random.choice(sexo))
    print('-' * 20)
    print(f'Nome: {nomet}')
    print(f'idade: {idade}')
    print(f'sexo: {sexot}')
    print('-' * 20)
    somaidade += idade
    if sexot in 'Masc' and idade > int(idadeM):
        nomeM = nomet
    if sexot in 'Fem' and idade < 20:
        fem20 += 1
mediaidade = somaidade / 4
print(f'A media de idade desse grupo é {mediaidade}')
print(f'O homem mais velho é {nomeM}')
print(f'Tem um total de {fem20} mulher abaixo dos 20 anos')