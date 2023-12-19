s = ''
s = input('Qual o seu sexo? [M/F] ').upper().strip()[0]
while s not in 'MF':
    print('Incorreto.')
    s = input('Qual o seu sexo? ').upper().strip()[0]
print(':)')