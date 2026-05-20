import random
v = 0 
while True:
    jogador = int(input('Diga o valor: '))
    comp = random.randint(0, 10)
    total = jogador + comp
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp} o total é {total}.')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    
    print('Vamos jogar novamente...\n')
print(f'\nGAME OVER! Você ganhou {v} vezes!')