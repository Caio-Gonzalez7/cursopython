v = float(input('Digite seu salario R$'))

if v > 1250.00:
    a = v * 0.10 + v
    print('Seu novo salario com o aumento de 10% é R${:.2f}'.format(a))
elif v <= 1250.00:
    b = v * 0.15 + v
    print('Seu novo salario com o aumento de 15% é de R${:.2f}'.format(b))