lista = []
dados = []
continua = True
while continua:
    for c in range(0, continua):
        print('---Se desejar sair digite -1---')
        dados.append(str(input('Digite o nome: ')))
        dados.append(int(input('Digite a idade: ')))
        for p in lista:
            if p[1] in dados