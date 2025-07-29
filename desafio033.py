a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))

if a > b and a > c:
    maior = a
elif b > c and b > a:
    maior = b
else:
    maior = c

if a < b and a < c:
    menor = a
elif b < c and b < a:
    menor = b
else:
    menor = c


print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
