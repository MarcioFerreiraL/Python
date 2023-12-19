import random
classificacao = ('Palmeiras', 'Gremio', 'Atletico Mineiro', 'Flamengo', 'Botafogo', 'Red Bull Bragantino', 'Fluminense', 'Atletico Paranaense', 'Internacional', 'Fortaleza', 'Sao Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'America')
def print_divisor():
    print("-" * 65)
print_divisor()
print('Os primeiros 5 colocados do brasileirão são respectivamente:')
for posicao, time in enumerate(classificacao[:5], start=1):
    print(f'{posicao} - {time}')
print_divisor()
print('Os últimos colocados do brasileirão são:')
for posicao, time in enumerate(classificacao[-4:], start=len(classificacao) - 3):
    print(f'{posicao} - {time}')
print_divisor()
print('Times em ordem alfabética:')
for i in range(0, len(sorted(classificacao)), 4):
    print(' - '.join(sorted(classificacao)[i:i+4]))
print_divisor()
T = random.choice(classificacao)
print(f'O {T} está na posição: {classificacao.index(T) + 1}')