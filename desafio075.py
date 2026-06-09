n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'Você digitou os valores {n}')

if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado!')

if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}.')

else:
    print('O valor 3 não foi digitado!')

print(f'Os valores pares foram: ', end = '')

for num in n:
    if num % 2 == 0:
        print(num, end=' ')
