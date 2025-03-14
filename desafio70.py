precop = 0
total = 0

while True:
    nomep = str(input('Nome do produto: ')).strip()
    precop = int(input('Preço R$: '))
    total += precop
    menor = float('inf')
    if menor > precop:
        menor = precop

    while True:
        try:         
            desejo = str(input('Deseja continuar? [S/N]: ')).strip().lower()
            if desejo not in ['s', 'n']:
                raise ValueError('Você digitou incorretamente, digite novamente.')
        except ValueError:
            print('Você digitou errado, digite novamente.')
            if desejo == 'n':
                print(f'O total foi de: {total}, menor foi de {menor}')
                break
            elif desejo == 's':
                print('Você escolheu continuar!')