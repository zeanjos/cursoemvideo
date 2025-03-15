valor = int(input('Qual valor você irá sacar? '))
cem = cinq = vin = dez = cin = um = 0

while True:
        if valor >= 100:
            valor -= 100
            cem += 1
        elif valor >= 50:
            valor -= 50
            cinq += 1
        elif valor >= 20:
            valor -= 20
            vin += 1
        elif valor <= 19:
            valor -= 10
            dez += 1
        elif valor < 10:
            valor -= 5
            cin += 1
        elif valor < 5:
            valor -= 1
            um += 1
        if valor == 0:
            break
print(f'Foram entregues {cem} notas de cem, {cinq} notas de cinquenta, {vin} notas de vinte, {dez} notas de dez, {cin} notas cinco e {um} moedas de um real')
