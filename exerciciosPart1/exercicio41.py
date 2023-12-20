import random
idade = random.randint(5,30)
if idade <= 9:
    print(f'Sua idade é {idade} e está na categoria MIRIM')
elif idade <= 14:
    print(f'Sua idade é {idade} e está na categoria INFANTIL')
elif idade <= 19:
    print(f'Sua idade é {idade} e está na categoria JUNIOR')
elif idade <= 20:
    print(f'Sua idade é {idade} e está na categoria SENIOR')
elif idade > 20:
    print(f'Sua idade é {idade} e está na categoria MASTER')