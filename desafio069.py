cont_sexo = 0
cont_idade = 0
cont_mulheres = 0

while True:
    
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] 
    
    if idade >= 18:
        cont_idade += 1
    
    if sexo == 'M':
        cont_sexo += 1
    
    if sexo == 'F' and idade <= 20:
        cont_mulheres +=1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]    
    if resp == 'N':
        break

print(f'Tem {cont_idade} pessoas com mais de 18 anos.')
print(f'Tem {cont_sexo} homens cadastrados.')
print(f'Tem {cont_mulheres} mulheres com menos de 20 anos.')
print('ACABOU!')