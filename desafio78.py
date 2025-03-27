from math import inf
menor = inf
maior = 0
num = []
for contagem in range(0, 5):
    num.append(int(input('Digite um número: ')))
for c, v in enumerate(num):
    if menor > num[c]:
        menor = num[c]
        indice = c
    if maior < num[c]:
        maior = num[c]
        indice_maior = c
print(f'O menor número digitado foi: {menor} no indice {indice}.\nO maior número digitado foi: {maior} no indice: {indice_maior}')