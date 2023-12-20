nome = input('Digite o seu nome: ').strip()
dividido = nome.split()
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu ultimo nome é {}'.format(dividido[2]))

# não consigo filtrar so para pegar o ultimo nome
