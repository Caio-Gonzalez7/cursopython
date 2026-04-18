from datetime import date

atual = date.today().year
menor = 0
maior = 0
for c in range (1,8):
    data = int(input(f'Qual o ano a {c}º pessoa nasceu? '))
    idade = atual - data
    
    if idade >= 21:
        maior += 1
    else:
        menor -= -1
print(f'Ao todo tivesmo {maior} mariores de idade e {menor} menores de idade! ')