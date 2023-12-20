import random
p = fem20 = homensT = 0
sexo = ['Masc', 'Fem']
C = 'S'
while True:
    if C == 'N':
        break
    elif C == 'S':
        idade = random.randint(1, 100)
        sexot = str(random.choice(sexo))
        print('-' * 20)
        print(f'idade: {idade}')
        print(f'sexo: {sexot}')
        print('-' * 20)
        if sexot in 'Masc':
            homensT += 1
        if sexot in 'Fem' and idade < 20:
            fem20 += 1
        if idade > 18:
            p += 1
    else:
        print('\033[2merror')
    C = input('Quer continuar? [S/N] ').upper().strip()[0]
print('\033[1;33mEsse foi o resultado da pesquisa:')
print(f'\033[34m{p} pessoas são maiores de 18 anos.')
print(f'\033[35m{homensT} homens foram cadastrados.')
print(f'\033[36m{fem20} mulheres tem mais de 20 anos.')