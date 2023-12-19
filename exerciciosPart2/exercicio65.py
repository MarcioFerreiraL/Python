import random
x = []
while True:
    num = random.randint(1, 100)
    print('-' * 10)
    print(num)
    print('-' * 5)
    x.append(num)
    r = input('Quer continuar? (S/N): ').strip().upper()[0]
    if r != 'S':
        break
maior = max(x)
menor = min(x)
media = sum(x) / len(x)
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')
print(f'A média dos números foi: {media:.2f}')
