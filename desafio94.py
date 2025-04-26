
lista_pessoas = []
cont = 0
soma = media = quantia_homens = quantia_mulheres = 0
while True:
    cont += 1
    dicionario_pessoas = {}
    dicionario_pessoas['nome'] = str(input(f'Digite o nome da {cont}ª Pessoa, "[N]" para sair: ').strip().capitalize())
    dicionario_pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).upper().strip()
    dicionario_pessoas['idade'] = int(input('Digite a idade: ').strip())
    lista_pessoas.append(dicionario_pessoas)
    desejo = str(input('Deseja continuar? [S/N]: ')).upper()
    if desejo == 'S':
        print('Você escolheu continuar.')
    else:
        break
quantia = len(lista_pessoas)
for p in lista_pessoas:
    soma += p['idade']
    media = soma / quantia
    quantia_homens += p['sexo']
    quantia_mulheres
print('-'*30)
print(f'Foram cadastradas {quantia} Pessoas, média de idade: {media:.2f}, foram cadastrado {quantia_homens} Homens')