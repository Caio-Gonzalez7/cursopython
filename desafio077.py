palavras = ("python", "programacao", "tupla", "string",
            "float", "codigo", "variavel", "funcao")
for p in palavras:
    print(f'\nNa palavras {p} temos ( ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra} )', end=' ')