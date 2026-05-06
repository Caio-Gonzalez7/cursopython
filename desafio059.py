n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = 0
menu = 0

while menu != 5:
    menu = int(input('[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nEscolha uma opção: '))
    if menu == 1:
        print(f'\nO valor da soma de {n1} + {n2} = {n1 + n2}\n')
print('Fim do programa!')