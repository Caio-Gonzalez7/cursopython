frase = str(input('Digite uma frase: ')).strip().upper()

qntA = frase.count('A')
procA = frase.find('A') + 1
procAF = frase.rfind('A') + 1

print('Nessa frase tem {} letras A'.format(qntA))
print('A primeira letra A aparece na posição {}'.format(procA))
print('A ultima letra A aparece na prosição {}'.format(procAF))