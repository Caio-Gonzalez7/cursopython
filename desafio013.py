s = float(input('Digite o valor do seu salario? R$'))

a = s * (15 / 100)
sa = s + a

print('O valor do aumento é de R${:.2f}, seu novo salário é de R${:.2f}'.format(a, sa))