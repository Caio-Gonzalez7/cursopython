#Escreva um programa que leia um valor em metros e o exiba convertido em centrímentros e milímetros

n1 = int(input('Digite uma media em metros: '))

c = n1 * 100
mm = n1 * 1000

print('Em centímetros {}cm e em milímetros {}mm'.format(c, mm))