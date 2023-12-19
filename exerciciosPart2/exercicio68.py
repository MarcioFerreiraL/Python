import random
r = V = D = 0
jogar = ['Par', 'Impar']
while True:
    E1 = random.choice(jogar)
    E2 = random.choice(jogar)
    print(f'O jogador1 escolheu {E1} e o jogador 2 escolheu {E2}')
    C1 = random.randint(0, 10)
    C2 = random.randint(0, 10)
    print(f'O jogador1 jogou {C1} e o jogador 2 jogou {C2}')
    print(f'E deu ')
    r = C1 + C2
    if r % 2 ==0:
        print('Deu PAR')
    else:
        print('Deu IMPAR')
    if E1 == 'Par':
        if r % 2 == 0:
            print('O Jogador1 VENCEU!')
            V += 1
        elif r % 2 != 0:
            print('O Jogador2 VENCEU!')
            D += 1
    if E1 == 'Impar':
        if r % 2 == 0:
            print('O Jogador2 VENCEU!')
            D += 1
        elif r % 2 != 0:
            print('O Jogador1 VENCEU!')
            V += 1
    if D >= 1:
        break
    print('-' * 60)
    print('Outra RODADA :)')
if V <= 1:
    print(f'\033[34mInfelizmente o Jogador1 venceu apenas {V} :(')
else:
    print(f'\033[34mO total de vitorias consecutivas do jogador1 foi {V} :)')