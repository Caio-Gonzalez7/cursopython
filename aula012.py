nome = str(input('Digite seu nome: '))
if nome == 'Caio':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é tão normal!')
print('Tenha um bom dia, {}!'.format(nome))