nome = str(input('Digite seu nome completo: ')).strip()

primeiro = nome.split()[0]
ultimo = nome.split()[-1]

print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(primeiro))
print('Seu ultimo nome é: {}'.format(ultimo))