import random
c = 0
valor = random.uniform(200, 2000)
print(f'O produto custa {valor:.2f}R$')
print("""
        ESCOLHA A FORMA QUE QUER PAGAR:
        
        À vista - 10% de desconto (digite 1)
        À vista no cartão - 5% de desconto (digite 2)
        2x no cartão (digite 3)
        3x no cartão - 20% de juros (digite 4)
        """)
pagamento = int(input(''))
if pagamento == 1:
    valor = valor * 0.9
    print(f'O valor a ser pago será: {valor:.2f}R$')
elif pagamento == 2:
    valor = valor * 0.95
    print(f'O valor a ser pago será: {valor:.2f}R$')
elif pagamento == 3:
    parcela = valor / 2
    print(f'O valor a ser pago será: {valor:.2f}R$ e a parcela será de {parcela:.2f}R$ ')
elif pagamento == 4:
    parcela = (valor * 1.2) / 3
    valorT = valor * 1.2
    print(f'O valor a ser pago será: {valorT:.2f}R$ e a parcela será de {parcela:.2f} R$')
else:
    print('error')
