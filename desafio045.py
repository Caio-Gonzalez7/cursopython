import random 

print('JOGO PEDRA, PAPEL, TESOURA')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2) 

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input ('Qual a sua jogada? '))

if computador == jogador:
    print('O jogo empatou!!')

elif computador == 0 and jogador == 1:
    print('Você ganhou!!')

elif computador == 1 and jogador == 0:
    print('O computador ganhou!!')

elif computador == 2 and jogador == 1:
    print('O computador ganhou!!')

elif computador == 1 and jogador == 2:
    print('Você ganhou!!')

elif computador == 0 and jogador == 2:
    print('O computador ganhou!!')

elif computador == 2 and jogador == 0:
    print('Você ganhou!!')