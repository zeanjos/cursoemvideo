lista = []
dados = []
menor = []
maior = []
continua = True
contador = 0
while continua:
    contador += 1
    
    dados.append(str(input(f'Digite o nome da {contador}ª Pessoa: ')).capitalize().strip())
    dados.append(float(input(f'Digite o peso da {contador}ª Pessoa: ')))
    lista.append(dados[:])
    
    if contador == 1:
        menor = dados[1]
        maior = dados[1]
    if dados [1] < menor:
        menor = dados [1]
    if dados [1] > maior:
        maior = dados [1]
    dados.clear()

    desejo = str(input('Deseja continuar [S/N]? '))
    if desejo == 's':
        print('Você escolheu continuar.')
    if desejo == 'n':
        print('-'*30)
        print('Você escolheu parar')
        continua = False

print('-'*30)
print(f'\nOs dados foram: {lista} e menor também: {menor}\nAo todo você cadastrou {len(lista)} Pessoas.\n')
print('-'*30)