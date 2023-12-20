import random
km = random.randint(60, 200)
if km > 80:
    p = (km - 80) * 7
    print('Você passou dos limites!, então terá que pagar {}R$'.format(p))
    print('OBS: sua velocidade foi de {}km'.format(km))
else:
    print('muito bem :) continue assim.')
    print('sua velocidade foi de {}km'.format(km))