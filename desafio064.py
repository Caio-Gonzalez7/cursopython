n = cont = total = 0

n = int(input('Digite um numero inteiro! [999 para parar]: '))

while n != 999:
    cont += 1  
    total += n
    n = int(input('Digite um numero inteiro! [999 para parar]: ')) 

print('A quantida de números digitados foi {}, e a soma deles foi {}'.format(cont, total))
print('FIM!')