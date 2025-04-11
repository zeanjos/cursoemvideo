matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um numero para a posição {linha}, {coluna} : '))
        matriz[linha] [coluna] = num
print('-'*30,'Matriz:','-'*30)
for linha in matriz:
    print(linha)
print('-'*60)
print('-'*30, 'Coluna:','-'*30)
for coluna in matriz:
    print(coluna)
print('-'*60)
