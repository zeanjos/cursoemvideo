idade = contm = contf = maior = menorf = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().lower()
    if sexo == 'm':
        contm += 1
    else:
        contf += 1
    if sexo == 'f' and idade < 20:
        menorf += 1
    desejo = str(input('Deseja continuar? [S/N]: '))
    if desejo == 'n':
        print('Você escolheu sair!')
        break
    else:
        print('Você escolheu continuar!') 
print(f'''{maior} Pessoas tem mais de 18 anos.\n
foram cadastrados {contm} {'Homem' if contm == 1 else 'homens'}.\n
{menorf} Mulheres tem menos de 20 Anos.''')