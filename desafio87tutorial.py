matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
soma_par = maior =  soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para o indice [{linha}] [{coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end = '')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print('-'*30)
print(f'A soma dos numeros pares é: {soma_par}')
print('-'*30)
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'Os valores somados da terceira coluna são: {soma_coluna}')
print('-'*30)
for c in range(0, 3):
    if maior < matriz[1][c]:
        maior = matriz[1][c]
print(f'O maior valor digitado da segunda linha foi: {maior}')
print('-'*30)