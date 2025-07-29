from datetime import date
ano = int(input('Digite um ano, e descubra se é um ano bissexto, coloque 0 para saber sobre o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print('O ano {} É um ano bissexto.'.format(ano))
else:
    print('O ano {} NÃO é um ano bissexto.'.format(ano))