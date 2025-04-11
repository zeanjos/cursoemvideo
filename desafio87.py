matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
terceira_coluna = maior = par = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um número para a posição: [{linha}], [{coluna}]: '))
        if num % 2 == 0:
            par += num
        if coluna == 2:
            terceira_coluna += num
        matriz[linha] [coluna] = num
        if linha == 1:
            if maior < num:
                maior = num
print('-'*30)
print('A matriz com os números digitados: ')
for linha in matriz:   
    print(linha)
print(f'A soma dos valores da terceira coluna é {terceira_coluna}\nO maior valor da segunda linha é {maior}')