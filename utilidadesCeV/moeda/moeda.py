def aumentar(num, num2=0):
    print(f'O numero R${num} aumentando 10% vale R${num * 1.1:.2f}')
    if num2 != 0:
        print(f'O numero R${num2} aumentando 10% vale R${num2 * 1.1:.2f}')
def diminuir(num, num2=0):
    print(f'O numero R${num} diminuindo 10% vale R${num * 0.9:.2f}')
    if num2 != 0:
        print(f'O numero R${num2} diminuindo 10% vale R${num2 * 0.9:.2f}')
def dobro(num, num2=0):
    print(f'O dobro de R${num} é R${num * 2}')
    if num2 != 0:
        print(f'O dobro de R${num2} é R${num2 * 2:.2f}')
def metade(num, num2=0):
    print(f'A metade de R${num} é R${num * 0.5}')
    if num2 != 0:
        print(f'A metade R${num2} é R${num2 * 0.5:.2f}')
def resumo():
    print('digite algum numero e irá ser mostrado o valor dele aumentado, diminuido, o doblo e a metade dele.')
# exercicio108, 109 e 110