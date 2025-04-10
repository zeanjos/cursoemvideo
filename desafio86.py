matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um numero para a posição {linha}, {coluna} : '))
        matriz[linha] [coluna] = num
print(matriz[linha])