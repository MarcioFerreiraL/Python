num = int(input('Digite um numero: '))
m = int(input(f'Quantas vezes multiplicar o numero {num}? '))
for c in range(0, m + 1):
    print(f'{num} x {c:>2} = {num * c}')