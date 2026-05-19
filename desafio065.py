prox = 'Ss'
cont = 0
soma = 0

while prox in 'Ss':
    cont += 1
    n = int(input('Digite um número: '))
    prox = str(input('Quer continuar? [S/N]: '))
    soma += n
    if cont == 1:
        maior = menor = n 
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont

print('Você digitou {} números, e a média é {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor valor {}'.format(maior, menor))
print('FIM!')