import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

# Determina o maior número usando a função max()
maior_numero = max(num1, num2, num3)

# Determina o menor número usando a função min()
menor_numero = min(num1, num2, num3)

# Mostra o resultado na tela
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")