dados = []
contador = 0
continua = True
while continua:
    contador += 1
    nome = str(input(f'Digite o nome do {contador} Aluno: ')).strip().capitalize()
    nota = float(input(f'Digite a primeira nota do aluno {nome}: '))
    segunda_nota = float(input(f'Digite a segunda nota do aluno {nome}: '))
    media = (nota + segunda_nota) / 2
    aluno = [nome, nota, segunda_nota, media]
    dados.append(aluno)

    desejo = str(input('Deseja cadastrar outra nota de aluno [S/N]? ')).lower()
    if desejo not in ['s', 'n']:
        print('Entrada inválida. Por favor, insira "S" para continuar ou "N" para sair.')
        break
    if desejo == 's':
        print('Sua escolha foi continuar!')
    elif desejo == 'n':
        break
print(dados)
    
    