soma = cont = menor = valores = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Valor do Produto: R$'))
    valores += 1
    soma += valor
    
    if valor >= 1000:
        cont += 1
    
    if valores == 1:
        menor = valor
        barato = nome
   
    else:
        if valor < menor:
            menor = valor
            barato = nome
         
    resp = ' '    
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if resp == 'N':
        break

print(f'O valor total da compra foi R${soma:.2f} reais.')
print(f'Ao todo tem {cont} produtos com valor maior de R$1000.00 reais.')
print(f'O item mais barato foi {barato} com valor de R${menor:.2f} reais.')
print('{:-^40}'.format(' FIM DO PROGRAMA! '))