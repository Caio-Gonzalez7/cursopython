a = int(input('Valor da primeira reta: '))
b = int(input('Valor da segunda reta: '))
c = int(input('Valor da terceira reta: '))

if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print('Forma um triangulo EQUILÁTERO!')
    elif a == b or a == c or b == c:
        print('Forma um triangulo ISÓSCELES!')
    else:
        print('Forma um triangulo ESCALENO!')
else:
print('Não forma triangulo!')