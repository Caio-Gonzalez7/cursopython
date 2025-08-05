print('\033[1;32mConsulta de emprestimo, esse programa irá te mostrar se você está apto a pegar um empréstimo.\033[m')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
parcela = casa / (anos *12)
if salario * 0.3 >= parcela:
    print('Emprestimo aprovado!!! O valor da parcela foi de R${:.3f}'.format(parcela))
else:
    print('Uma pena, emprestimo negado, pois a parcela de R${:.3f} excede 30% do seu salário.'.format(parcela))