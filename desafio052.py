n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print(f'\n\033[mO número {n} foi divísivel {total} vezes')