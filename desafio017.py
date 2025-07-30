import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(oposto, adjacente)

print('A hipotenusa dos catetos respectivamente, oposto {:.2f} e adjacente {:.2f}. Sendo assim a hipotenusa é = {:.2f}'.format(oposto, adjacente, hipotenusa))