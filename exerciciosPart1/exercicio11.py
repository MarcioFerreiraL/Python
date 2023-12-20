a = float(input('Quanto mede a altura da parede(m)? '))
l = float(input('Quanto mede a largura da parede(m)? '))
p = a * l
t = 0.5 * p
print('Sua parede tem {} m² e será necessário ter {}L de tinta para pinta-la'.format(p, t))