numeros = []
continua = True
while continua:
    num = (int(input('Digite um número, digite um número negativo se desejar parar: ')))
    if num in numeros:
        print('Este número já existe na lista, não será adicionado.')
    else:
        numeros.append(num)
    if num < 0:
        print('Voce decidiu parar.')
        numeros.pop()
        continua = False
numeros.sort()
print(f'Os números da lista em ordem crescente são: {numeros}')