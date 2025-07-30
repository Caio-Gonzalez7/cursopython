#Crie um algoritimo que leia um número e mostre seu dobro, tripo e sua raiz quadrada#


n1 = int(input('Digite um valor '))

d = n1*2
t = n1*3
raiz = n1**(1/2)

print('O dobro de {} é {}\nO tripo de {} é {}\nA raiz quadrada de {} é {:.2f}'.format(n1,d,n1,t,n1,raiz))