lista = []
dados = []
continua = True
menor_peso_nome = maior_peso_nome = []
while continua:
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
    if not menor_peso_nome:
        menor_peso_nome = [p[0], p[1]]
    if not maior_peso_nome:
        maior_peso_nome = [p[0], p[1]]
    if p[1] > maior_peso_nome[1]:
        maior_peso_nome = [p[0], p[1]]
    if p[1] < menor_peso_nome[1]:
        menor_peso_nome = [p[0], p[1]]
tamanho_lista = len(lista)
print('-'*30)
print(f'Você cadastrou {tamanho_lista}\n Pessoas Maior peso {maior_peso_nome}\n Menor peso {menor_peso_nome}')