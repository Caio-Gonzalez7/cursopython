n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))

media = (n1 + n2) / 2 

if media <= 4.9:
    print('Sua media foi \033[1;31m{}\033[m, uma pena mas você foi \033[1;31mREPROVADO!!!\033[m'.format(media))

elif media >= 5.0 and media <= 6.9:
    print('Sua media foi \033[1;33m{}\033[m, você tem o direito de fazer a \033[1;33mRECUPERAÇÃO!!!\033[m'.format(media))

elif media >= 7.0:
    print('Sua media foi \033[1;32m{}\033[m, parabéns você foi \033[1;32mAPROVADO!!!\033[m'.format(media))