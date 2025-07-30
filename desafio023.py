numero = input('Digite um numeor de 0 a 9999: ')

unidade = numero[:5]
dezena = numero[2:3].lstrip()
centena = numero[1:2]
mil = numero[0]

print('Unidade: {}'.format(unidade[:5]))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(mil))