lista_aluno = {}
nome = []
média = []
situation = 7
while True:
    lista_aluno['nome'] = str(input('Nome: ')).capitalize().strip()
    lista_aluno['media'] = float(input(f'Média de {lista_aluno['nome']}: '))
    print(f'Nome é igual a {lista_aluno['nome']}')
    print(f'Média é igual a {lista_aluno['media']}')
    if lista_aluno['media'] >= situation:
        print('Situação igual a aprovado.')
    else:
        print('Situação é igual a reprovado.')
    break