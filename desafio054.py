maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite ano do seu nascimento: '))
    
    if 2026 - ano >= 18:
        maior = maior + 1
    
    elif 2026 - ano <= 17:
        menor = menor + 1
print(f'Das sete pessoas {maior} são maiores de idade e {menor} são menor de idade')