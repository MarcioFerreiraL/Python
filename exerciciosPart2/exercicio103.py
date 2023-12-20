def ficha(b=0, c=0):
    if b == 1 or c == 1:
        print('Jogador1 - 1 gol')
    elif b == 2 or c == 2:
        print('Jogador2 - 2 gols')
    elif b == 3 or c == 3:
        print('Jogador3 - 3 gols')
    elif b == 4 or c == 4:
        print('Jogador4 - 4 gols')
    elif b == 5 or c == 5:
        print('Jogador5 - 5 gols')
    elif b == 6 or c == 6:
        print('Jogador7 - 7 gols')
    elif b == 7 or c == 7:
        print('Jogador8 - 8 gols')
    elif b == 8 or c == 8:
        print('Jogador9 - 8 gols')
    elif b == 9 or c == 9:
        print('Jogador10 - 9 gols')
    elif b == 10 or c == 10:
            print('Jogador10 - 10 gols')
    else:
        print('error.')
        print('digite corretamente (1 a 10)')
from random import randint
numero = ficha(randint(0, 10), randint(0, 10))