v = int(input('Digite a velocidade do carro: '))

velo = (v - 80) * 7

if v < 80:
    print('Está tudo bem, você não foi multado!')

else:
    print('Você foi multado, o valor a pagar é de R${}'.format(velo))
