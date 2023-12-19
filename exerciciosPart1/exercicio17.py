import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = pow(ca, 2) + pow(co, 2)
print('a hipotenusa é igual a {:.2f}'.format(math.sqrt(h)))
