A = float(input('Altura da parede: '))
L = float(input('Largura da parede: '))

a2 = A*L
t = a2/2

print('A á rea da parede é de {:.2f}m², assim para pintar será necessário {:.2f}l de tinta'.format(a2, t))