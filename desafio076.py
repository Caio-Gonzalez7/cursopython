listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Mochila', 159.99,
            'Estojo', 20,)

print('-' * 38)
print(f'{"LISTAGEM DE PREÇO":^37}')
print('-' * 38)

for pos in range(0, len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>.2f}')
print('-' * 38)