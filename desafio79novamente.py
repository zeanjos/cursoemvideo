from math import inf
menor = inf
num = []
continua = True
parar_loop = 0
indice_menor = indice_maior = -1


while continua:
    numero = int(input('Digite um número, digite 0 se desejar parar: '))
    maior = numero
    if numero in num:
        print('Este número já existe na lista, não será adicionado.')
        num.pop()

    if numero == parar_loop:
        continua = False
    else:
        num.append(numero)
    for i, v in enumerate(num[0:]):
        if menor > v:
            menor = v
            indice_menor = i
        if maior < v:
            maior = v
            indice_maior = i

print(f'O menor valor da lista: {menor} no indice: {indice_menor}, O maior número da lista: {maior} no indice: {indice_maior}')