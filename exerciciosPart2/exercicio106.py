def puxarHelp(frase):
    help(frase)
while True:
    print('Quer continuar? ')
    print('Se nao, digite "FIM"')
    print('Se sim, digite "SIM"')
    confirmation = input().upper().strip()
    if confirmation == 'FIM':
        break
    elif confirmation == 'SIM':
        puxarHelp(input('Digite algum operador que voce quer ver o manual: '))
        print('='*30)
    else:
        print('error')