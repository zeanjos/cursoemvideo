

num = []
indice_menor = []

for contagem in range(0, 5):
    num.append(int(input('Digite um número: ')))
for c, v in enumerate(num):
    if menor_num > num[c]:
        menor_num = num[c]
