n = int(input('Digite um número para saber se é primo: '))
for c in (2, 23):
    primo = n % c
if primo >= 1:
    print('O numero {} é um numero primo!'.format(n))
elif primo == 0:
    print('Não é um numero primo!')