v = float(input('Digite o valor do produto: '))

dc = v - (v * 0.10)
ca = v - (v * 0.05)
c2 = v 
c3 = v + (v * 0.20)

print('\nDinheiro/cheque com 10% off\nCartão à vista 5% off\n2x no cartão, valor normal\n3x ou mais no cartão 20% de acréscimo\n')

1 == dc
2 == ca
3 == c2
4 == c3

p = int(input('Para escolher cartão/cheque digite 1\nPara escolher cartão à vista digite 2\nPara escolher 2x no cartão digite 3\nPara escolher 3x ou mais no cartão digite 4\nQual a sua escolha? '))

if p == 1:
    print('O valor do produto com desconto por pagamento com dinheiro/cheque é de 10%, o valor passou a ser R${:.2f}'.format(dc))
elif p == 2:
    print('O valor do produto com desconto por pagamanto à vista com cartão é de 5%, o valor a pagar é de R${:.2f}'.format(ca))
elif p == 3:
    print('O valor a pagar é o mesmo de R${:.2f}'.format(c2))
elif p == 4:
    print('O valor do produto com o acréscimo por pagamento em mais de 3x no cartão é de 20%, o vcalor a ser pagou é de R${:.2f}'.format(c3))