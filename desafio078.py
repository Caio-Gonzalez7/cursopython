print('DIGITE 5 VALORES PARA DESCOBRIR QUAL O MAIOR DENTRO DA LISTA')
valores = []
maior = 0 
menor = 0


for cont in range(0,5):
    valores.append(int(input(f'Digite o valor para posição {cont}: ')))

    if cont == 0:
        maior = menor = valores[cont]

    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores [cont] < menor:
            menor = valores[cont]

print('=-'*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor foi {maior} nas posições ', end='')

for i, v in enumerate(valores):
    if v == maior:
        print(f'|{i}| ',end='')

print()

print(f'O menor valor foi {menor} nas posições ', end='')

for i, v in enumerate(valores):
    if v == menor:
        print(f'|{i}| ',end='')