lista = []
dados = []
maior_peso = 0
menor_peso = None
continua = True
menor_peso_nome = []
while continua:
    for c in range(0, continua):
        dados.append(str(input('Digite o nome: ')))
        dados.append(int(input('Digite o peso: ')))
        lista.append(dados[:])
        dados.clear()
        desejo = str(input('Deseja continuar [S/N]?')).lower().strip()
        if desejo == 's':
            print('Voce escolheu continuar.')
        elif desejo == 'n':
            print('Voce desejou parar.')
            continua = False
        else:
            print('Voce digitou um caracter invalido.')
for p in lista:
    if menor_peso is None:
        menor_peso = p[1]
    if p[1] > maior_peso:
                maior_peso = p[1]
    if p[1] < menor_peso:
        menor_peso = p[0]
        menor_peso_nome = p[0], p[1]
tamanho_lista = len(lista)
print('-'*30)
print(f'Você cadastrou {tamanho_lista} Pessoas Maior peso {maior_peso}\n Menor peso {menor_peso_nome}')