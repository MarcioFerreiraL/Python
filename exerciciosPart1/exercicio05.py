n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
s = n1 + n2
su = n1 - n2
d = n1 / n2
r = n1 ** n2 / 2
m = n1 * n2
di = n1 // n2
dr = n1 % n2
p = n1 ** n2
print('A soma é {}, a subtração é {}, a divisão é {:.2f}, a raiz quadrada é {:.2f}'.format(s, su, d, r), end=' ')
print('A multiplicação é {}, a divisão inteira é {}, o resto da divisão é {}, a potenciação é {}'.format(m, di, dr, p))
