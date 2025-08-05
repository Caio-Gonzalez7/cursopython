from datetime import date
ano = int(input('Digite o ano que você nasceu para saber sobre o seu alistamento! '))
data = date.today().year
idade = data - ano
print('Você tem {} anos'.format(idade))
if idade <= 17:
    print('Você ainda não possui a idade minima para se alistar. Ainda faltam {} anos para se alistar'.format(17 - idade))
elif idade <= 45:
    print('Você está na idade para se alistar!!')
elif idade >= 46:
    print('Você já passou da idade para o alistamento obrigatório. Já se passaram {} anos do prazo'.format(idade - 46))