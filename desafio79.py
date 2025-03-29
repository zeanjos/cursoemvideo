numeros = []
continuar = True
num_organizado = None
while continuar:
    num = int(input('Digite um número: '))
    if num in numeros:
        print('Este número já existe e não será adicionado')
    else:
        numeros.append(num)
    desejo = str(input('Deseja continuar [S/N]? ')).lower().strip()
    if desejo == 's':
        print('Você escolheu continuar!')
    if desejo == 'n':
        numeros.sort()
        print(f'Você escolheu parar, a lista em ordem com os números digitados: {numeros}')
        continuar = False
    if desejo not in ['s', 'n']:
        print('Você digitou um caracter incorreto!')
        continuar = False