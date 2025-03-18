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
        elif valor >= 10:
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
print(f'{'Foram entregues {cem} notas de cem,' if cem >= 1 else ''}\n { '{cinq} notas de cinquenta,' if cinq >= 1 else ''}\n { '{vin} notas de vinte,' if vin >= 1 else ''}\n { '{dez} notas de dez,' if dez >= 1 else ''}\n {'{cin} notas cinco' if cin >= 1 else ''} {'e {um} moedas de um real' if um >= 1 else ''}')
