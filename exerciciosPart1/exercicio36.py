<<<<<<< HEAD
valor = float(input('Qual o valor da casa?' ))
sal = float(input('Qual o valor do seu salário? '))
anos = int(input('Com quantos ano você pretende pagar a casa? '))
pm = valor / (anos * 12)
if pm > 0.3 * sal:
    print('Seu empréstimo foi negado.')
    print(f'Pois o valor da Prestação Mensal({pm}) foi acima de 30% do seu salario!')
else:
=======
valor = float(input('Qual o valor da casa?' ))
sal = float(input('Qual o valor do seu salário? '))
anos = int(input('Com quantos ano você pretende pagar a casa? '))
pm = valor / (anos * 12)
if pm > 0.3 * sal:
    print('Seu empréstimo foi negado.')
    print(f'Pois o valor da Prestação Mensal({pm}) foi acima de 30% do seu salario!')
else:
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print(f'o valor da prestação mensal que vc irá pagar é de {pm}')