#Desenvolva um progama que leia as duas notas de um aluno, calcule e mostre a sua media#

p1 = float(input('Nota da primeira prova = '))
p2 = float(input('Nota da segunda prova = '))

s = p1 + p2
m = s / 2

print('A media é {:.1f}'.format(m))