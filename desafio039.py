from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
data = date.today().year
idade = data - ano
print('Você tem {} anos'.format(idade))
if idade < 18:
    print('Você ainda não possui a idade minima para se alistar. Ainda faltam {} anos para se alistar'.format(18 - idade))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você deveria ter se alistado hà {} anos.'.format(idade - 18))