times = ("Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Red Bull Bragantino", "Coritiba", "São Paulo", "Bahia", "Cruzeiro", "Botafogo", "Vitória", "Atlético-MG", "Internacional", "Grêmio", "Corinthians", "Vasco", "Santos", "Mirassol", "Remo", "Chapecoense",)

print('A tabela atual é:\n')
print(times)

print('\nOs 5 primeiros times são:')
for time in times [0:5]:
    print(time)

print('\nOs 4 ultimos times são:')
for time in times [16:21]:
    print(time)

print('\nOs times em ordem alfabetica são:')
print(sorted(times))

print(f'\nO time da Chapecoense está na posição {times.index('Chapecoense')+1}\n')