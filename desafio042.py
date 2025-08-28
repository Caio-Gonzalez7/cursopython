a = int(input('Valor da primeira reta: '))
b = int(input('Valor da segunda reta: '))
c = int(input('Valor da terceira reta: '))

if a + b > c and b + c > a and c + a > b:
    print('Não forma triangulo!')

elif a == b == c:
    print('Forma um triangulo EQUILÁTERO!')

elif a == b  or a == c or c == b :
    print('Forma um triangulo ISÓCELES!')

elif a != b != c:
    print('Forma um triangulo ESCALENO!')
