n = float(input('Qual a distancia da sua viagem? '))

valor = n * 0.50
valor2 = n * 0.45

if n <= 200:
    print('O valor para sua passagem é de R${:.2f}, cosiderando R$0.50 por KM!'.format(valor))

else:
    print('O valor da passagem é de R${:.2f}, considerando R$0.45 por KM!'.format(valor2))
