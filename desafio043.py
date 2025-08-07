peso = float(input('Qual seu peso em KG: '))
altura = float(input('Qual sua altura: '))
IMC = peso / (altura ** 2)

if IMC <= 18.4:
    print('Você está abaixo do peso ideal, seu imc é {:.2f}'.format(IMC))

elif IMC <= 24.9:
    print('Você está no peso ideal, seu imc é {:.2f}'.format(IMC))

elif IMC <= 29.9:
    print('Você esta com sobrepeso, seu imc é {:.2f}'.format(IMC))

elif IMC <= 39.9:
    print('Você esta com obesidade, seu imc é {:.2f}'.format(IMC))

else:
    print('Você esta com obesidade mórbida, seu imc é {:.2f}'.format(IMC))