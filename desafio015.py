km = float(input('Quantos KM foram percorridos? '))
d = int(input('Quantos dias alugados? '))

pago = (km * 0.15) + (d * 60)

print('O total por {}KM e {} dias, foi de R${:.2f}'.format(km, d, pago))