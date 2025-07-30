import math
ang = float(input('Digite um angulo: '))

cos = math.cos(ang)
sin = math.sin(ang)
tan = math.tan(ang)

print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang,sin))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang,tan))
