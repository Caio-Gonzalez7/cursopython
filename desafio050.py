soma = 0
for c in range(1,7):
    n = int(input('Digite 6 numeros e veja a somas dos pares: '))
    if n % 2 == 0:
        soma += c   
print('A soma dos números pares é {}'.format(soma))