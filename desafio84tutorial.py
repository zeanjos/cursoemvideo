lista = []
dados = []
menor = 0
maior = 0
nome_menor = []
nome_maior = []
continua = True
contador = 0
while continua:
    contador += 1
    
    dados.append(str(input(f'Digite o nome da {contador}ª Pessoa: ')).capitalize().strip())
    dados.append(float(input(f'Digite o peso da {contador}ª Pessoa: ')))
    lista.append(dados[:])
    
    if len(lista) == 1:
        menor = maior = dados[1]
    else:
        if dados [1] < menor:
            menor = dados [1]

        if dados [1] > maior:
            maior = dados[1]
        dados.clear()

    desejo = str(input('Deseja continuar [S/N]? '))
    if desejo == 's':
        print('Você escolheu continuar.')
    if desejo == 'n':
        print('-'*30)
        print('Você escolheu parar')
        continua = False

print('-'*30)
for p in lista:
    if p[1] == maior:
        nome_maior = p[0]
print(f'O maior peso foi de {nome_maior} com {maior}kgs')
for p in lista:
    if p[1] == menor:
        nome_menor = p[0]
print(f'\nO menor peso foi de: {nome_menor} com {menor} Kgs\n\nAo todo você cadastrou {len(lista)} Pessoas.\n')
print('-'*30)