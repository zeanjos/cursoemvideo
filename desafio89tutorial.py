ficha = []
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    nota1 = float(input('Nota 1: ').strip())
    nota2 = float(input('Nota 2: ').strip())
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    while True:
        desejo = str(input('Quer continuar [S/N]? ')).lower().strip()
        if desejo in ['s', 'n']:
            break
        print('Entrada invalida. Por favor digite novamente.')
    if desejo == 's':
        print('Você escolheu continuar.')
    elif desejo == 'n':
        print('Você escolheu parar.')
        break
        
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')   
for i, a in enumerate(ficha):  
    print('-'*30)
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    desejo = int(input('Digite o Nº Que deseja visualizar as notas, digite [999] Se desejar sair: '))
    if desejo == 999:
            print('Você escolheu sair, até mais!')
            break
    if desejo < len(ficha):
        print(f'A nota do aluno {ficha[desejo][0]} Foi {ficha[desejo][1]}')
        