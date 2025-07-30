nome = input('Digite seu nome: ')

cap = nome.upper()
minu = nome.lower()
espacos = nome.replace(' ','')
total = len(espacos)
prim = nome.split()

print('Todas as letras maiúsculas: {}'.format(cap))
print('Todas as letras muinúcuslas: {}'.format(minu))
print('Tem o total de {} letras'.format(total))
print('O primeiro nome tem {} letras'.format(len(prim[0])))