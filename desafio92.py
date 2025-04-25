from datetime import datetime
ano_atual = datetime.now().year
anos = 35
candidato = {}
candidato['nome'] = str(input('Digite o nome: ')).strip().capitalize()
candidato['ano de nascimento'] = int(input('Ano de nascimento: ').strip())
candidato['carteira de trabalho'] = int(input('Carteira de trabalho (0 Não tem): ').strip())
if candidato['carteira de trabalho'] != 0:
    print('Possui carteira de trabalho.')
    candidato['ano de contratação'] = int(input('Ano de contratação: ').strip())
    candidato['salario'] = float(input('Salário: ').strip())
    aposentadoria = anos - (ano_atual - candidato['ano de contratação'])
    print('-'*30)
    print(f'Nome: {candidato['nome']},\nAno de nascimento: {candidato['ano de nascimento']},\nCarteira de trabalho: {candidato['carteira de trabalho']},\nAno de contratação: {candidato['ano de contratação']},\nSalário: {candidato['salario']:.2f},\nCarteira de trabalho: {candidato['carteira de trabalho']}')
    print(f'Faltam {aposentadoria} Anos para o candidato {candidato["nome"]} se aposentar.')
    print('-'*30)
else:
    print('-'*30)
    print('Não possui carteira de trabalho.')
    print(f'Nome: {candidato['nome']}\nAno de nascimento: {candidato['ano de nascimento']}')
    print('-'*30)
#if candidato['carteira de trabalho'] != 0:
    