from random import randint

computador = randint(0,10)

print('Sou seu computador... Acabei de pensar em um numero de 0 a 10.')
print('Sera que você consegue adivinhar? ')

acerto = False
palpites = 0

while not acerto:
    jogador = int(input('Qual o seu palpite: '))
    
    palpites += 1
    
    if jogador == computador:
        acerto = True
    
    else:
        if jogador < computador:
            print('Mais... Tente novamente: ')
        
        if jogador > computador: 
            print('Menos... Tente novamente: ')

print(f'Você acertou em {palpites} tentativas')