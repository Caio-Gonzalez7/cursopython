cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
resp = ' ' 

while True:
    
    n = int(input('Digite um número entre 0 e 20: '))

    
    if 0 <= n <=20:
        print(f'Você digitou o número {cont[n]}!')        
    
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    
    
    if resp == 'N':
        break    
