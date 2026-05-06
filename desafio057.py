m = 'M'
f = 'F'

while m == "M" or f == "F":
    sexo = str(input('Digite o sexo [M/F]: ')).upper()

    if sexo == "M":
        print('Sexo masculino!')

    elif sexo == "F":
        print('Sexo feminino!')

    else:
        print('Resposta invalida, digite M para masculino e F para feminino!')

print('Fim!')