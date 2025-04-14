dados = []
contador = 0
continua = True
while continua:
    contador += 1
    nome = str(input(f'Digite o nome do {contador} Aluno: ')).strip().capitalize()
    nota = float(input(f'Digite a primeira nota do aluno {nome}: '))
    segunda_nota = float(input(f'Digite a segunda nota do aluno {nome}: '))
    media = (nota + segunda_nota) / 2
    aluno = [nome, media]
    dados.append(aluno)

    while continua:
        desejo = str(input('Deseja cadastrar outra nota de aluno [S/N]? ')).lower()
        if desejo not in ['s', 'n']:
            print('Entrada inválida. Por favor, insira "S" para continuar ou "N" para sair.')
        if desejo == 's':
            print('Sua escolha foi continuar!')
            break
        elif desejo == 'n':
            print('Voce escolheu parar!')
            continua = False
print('-'*30)
print('Nº  Nome        Média')
dados_formatados = [[aluno[0], f'{aluno[1]:.2f}']for aluno in dados]
for i, enumerados in enumerate(dados_formatados):
    print(f'{i} - {" |      ".join(enumerados)}')

    