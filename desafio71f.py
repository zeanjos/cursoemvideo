valor = int(input('Digite o valor que quer sacar: '))
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
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 5:
        valor -= 5
        cin += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    if valor == 0:
        break
print(f'''Foram sacados {cem} Notas de cem\n
{cinq} Notas de cinquenta\n
{vin} Notas de vinte\n
{dez} Notas de dez\n
{cin} Notas de cinco\n
{um} Moedas de um real.''')
