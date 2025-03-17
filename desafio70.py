precop = 0
total = 0
menor = float('inf')
mil = 0
while True:
    nomep = str(input('Nome do produto: ')).strip()
    while True:    
        try:
            precop = float(input('Preço R$: '))
            break
        except ValueError:
            print('Opção invalida. Digite novamente.')
        
    total += precop
    if precop > 1000:
        mil += 1
    if menor > precop:
        menor = precop
        nome_menor = nomep
    while True:
        try:

            desejo = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
            if desejo not in ['s', 'n']:
                raise ValueError('Você digitou incorretamente.')
            elif desejo == 'n':
                print('Até mais!')
                break
            elif desejo == 's':
                print('Você escolheu continuar!')
                break
        except ValueError:
            print('Você digitou incorretamente, digite novamente.')
    
    if desejo == 'n':
        break

print(f'O total foi de: {total:.2f}, o produto mais barato foi o (a) {nome_menor} de valor {menor:.2f}, Quantidade de produtos acima de mil reais: {mil} ')