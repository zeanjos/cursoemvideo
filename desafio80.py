numeros = []
for i in range(0, 5):
    num = int(input('Digite um número:'))
    numeros.append(num)
for i in range(0, 5):
    for j in range(i+1, 5):
        if numeros[i] > numeros[j]:
            temp = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = temp
print(f'Números organizados: {numeros}')