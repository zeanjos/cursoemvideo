lista_menor = []
menor = []
num = []
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
    indice_menor = num.index(min(num))
    menor_num = min(num)
print(f'Menor número {menor_num}, no indice {indice_menor}')