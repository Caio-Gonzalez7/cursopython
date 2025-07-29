import random

n = int(input('Digite um numero de 0 a 5 para tentar vencer o computador: '))

lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)

print('O numero escolhido foi {}'.format(escolhido))

if n == escolhido :
    print('Parabéns, você ganhou!!!')
else:
    print('Uma pena, o computador ganhou!!!')