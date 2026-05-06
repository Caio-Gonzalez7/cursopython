import random

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(lista)


while escolhido == n:
    n = int(input('Digite um numero de 0 a 10 para tentar vencer o computador: '))
print(escolhido, n )