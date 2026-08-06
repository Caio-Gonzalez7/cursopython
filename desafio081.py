lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resp = str(input('QUER CONTINUAR? [S/N] ')).lower().strip()[0]
    if resp in 'n':
        break

print(f'Você digitou {len(lista)} elementos!')

lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')