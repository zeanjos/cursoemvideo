numeros = []
for i in range(0, 5):
    num = int(input(f'Digite o {i+1}º Número: '))
    numeros.append(num)
    if i == 0:
        print('Número adicionado ao final da lista.')
for i in range(0, 5):
    
    for j in range(i+1, 5):
        if numeros[i] > numeros[j]:
            temp = numeros[j]
            numeros[j] = numeros[i]
            numeros[i] = temp
for i in range(0, 5):
    print(f'Número {numeros[i]} adicionado no indice {i}')
print(f'Números ordenados {numeros}')