dados = []
peso = []
menor_peso = []

continua = True
contador = 0
while continua:
    contador += 1
    peso.append(str(input(f'Digite o nome da {contador}ª Pessoa: ')))
    peso.append(float(input(f'Digite o peso da {contador}ª Pessoa: ')))

    desejo = str(input('Deseja continuar [S/N]? '))
    if desejo == 's':
        print('Você escolheu continuar.')