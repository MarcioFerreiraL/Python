from random import choice
ca = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
cn = '1234567890'
ce = '!@#$%&*()?Çç'
letras = int(input('Quantas letras você quer na sua senha? '))
numeros = int(input('Quantos números você quer na sua senha? '))
caracteres = int(input('Quantos caracteres especiais você quer na sua senha? '))
totalSenha = letras + numeros + caracteres
senha = []
for _ in range(letras):
    senha.append(choice(ca))
for _ in range(numeros):
    senha.append(choice(cn))
for _ in range(caracteres):
    senha.append(choice(ce))
from random import shuffle
shuffle(senha)
senha_completa = ''.join(senha)
print(senha_completa)