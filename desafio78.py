from math import inf
menor = inf
maior = 0
num = []
lista_menor = indice_menor = []
for contagem in range(0, 5):
    num.append(int(input('Digite um número: ')))
for c, v in enumerate(num):
    if menor > num[c]:
        menor = num[c]
        indice = c
        if menor == num[c]:
            lista_menor.append(v)
            indice_menor.append(c)
    if maior < num[c]:
        maior = num[c]
        indice_maior = c
print(f'O menor número digitado foi: {menor} no indice {indice}.\nO maior número digitado foi: {maior} no indice: {indice_maior}, indice do menor 2x: {indice_menor}, lista do menor 2x: {lista_menor}')