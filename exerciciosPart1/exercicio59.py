x = 4
while x != 5:
    if x == 1:
        print(f'{num1:.2f} + {num2:.2f} = {num1 + num2:.2f}')
    elif x == 2:
        print(f'{num1:.2f} x {num2:.2f} = {num1 * num2:.2f}')
    elif x == 3:
        print(f'{num1:.2f} / {num2:.2f} = {num1 / num2:.2f}')
    elif x == 4:
        num1 = float(input('Escolha um valor: '))
        num2 = float(input('Escolha outro valor: '))
    elif x == 5:
        print('ok :)')
    else:
        print('error')
    print("""
------------------------
    [1] Somar
    [2] Multiplicar
    [3] Dividir
    [4] Novos Numeros
    [5] Sair
------------------------
    """)
    x = int(input(''))
