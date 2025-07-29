print('Analisandor de Triângulos')

p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if p1 + p2 > p3 and p1 + p3 > p2 and p2 + p3 > p1:
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('Os segmentos acima NÃO podem formar um triangulo')
