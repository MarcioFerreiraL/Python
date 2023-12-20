import random
km = random.randint(100,300)
print(km,'km')
if km <= 200:
    p = km * 1/2
    print('O preço da viagem será de {}R$'.format(p))
else:
    p = km * 45/100
    print('O preço da viagem será de {}R$'.format(p))