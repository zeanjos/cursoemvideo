idade = contm = contf = maior = menorf = 0
while True:
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            break
        except ValueError:
            print('Valor invalido. Digite um número.')
    if idade > 18:
        maior += 1
    while True:    
        try:
            sexo = str(input('Digite seu sexo: [M/F] ')).strip().lower()
            if sexo not in ['m', 'f']:
                raise ValueError
            break
        except ValueError:
            print('Valor invalido. Digite um sexo correto.')
    if sexo == 'm':
        contm += 1
    else:
        contf += 1
    if sexo == 'f' and idade < 20:
        menorf += 1
    desejo = str(input('Deseja continuar? [S/N]: '))
    while desejo != 's' and desejo != 'n':
        desejo = str(input('Deseja continuar? [S/N]: '))
    if desejo == 'n':
        print('Você escolheu sair!')
        break
    if desejo == 's':
        print('Você escolheu continuar!')

print(f'''{maior} Pessoas tem mais de 18 anos.\n
foram cadastrados {contm} {'Homem' if contm == 1 else 'homens'}.\n
{menorf} Mulheres tem menos de 20 Anos.''')
