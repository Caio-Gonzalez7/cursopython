frase = input('Digite uma frase: ')

frase_limpa = frase.replace(" ", "").lower()

if frase_limpa == frase_limpa[::-1]:
    print(f'A frase `{frase}` é um palíndromo.')
else:
    print('Está frase não é um palíndromo.')