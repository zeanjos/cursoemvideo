matriz = [
    [0, 0, 0],
    [0, 0, 0]
]
soma = 0
soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para o indice [{linha}] [{coluna}]'))
        if matriz[linha] [coluna] % 2 == 0:
            soma += matriz[linha] [coluna]
        if matriz[coluna] > 0:
            soma_coluna += matriz[coluna]
print(f'Pares {soma}\n Soma da coluna {soma_coluna}')
