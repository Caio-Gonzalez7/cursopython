n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = 0
menu = 0

while menu != 5:
    
    menu = int(input('[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nEscolha uma opção: '))
    
    if menu == 1:
        print(f'\nO valor da soma de {n1} + {n2} = {n1 + n2}.\n')
    
    elif menu == 2:
        print(f'\nO valor da multiplicação entre {n1} * {n2} = {n1 * n2}.\n')

    elif menu == 3: 
        if n1 > n2:
            print(f'\nO maior valor entre {n1} e {n2} é o número {n1}.\n')
        else:
            print(f'\nO maior valor entre {n1} e {n2} é o número {n2}.\n')
    elif menu == 4:
        print('Digite novamente!')
        n1 = int(input('Escolha o novo número: '))
        n2 = int(input('Escolha o mais um novo número: '))

print('Fim do programa!')