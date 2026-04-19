soma_grupo = 0

maior_idade_homem = 0

nome_velho = ''

mulher20 = 0

for c in range(1,4):
    
    print(f'------------{c}ª PESSOA------------')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str.upper(input('M/F: '))
    soma_grupo += idade
    
    if c == 1 and sexo in 'M':
        maior_idade_homem = idade
        nome_velho = nome
    
    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'F' and idade < 20:
        mulher20 += 1

print(f'A media da idade do grupo é {soma_grupo / c:.2f} anos!')

print(f'O homem mais velho se chama {nome_velho} e a idade dele é {maior_idade_homem} anos!')

print(f'Tem {mulher20} mulheres com menos de 20 anos!')