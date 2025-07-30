a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Os valores digitados formam um triangulo')
else:
    print('Os valores digitados não formam um triangulo')