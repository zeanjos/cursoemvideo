lista_numeros = []
numeros = []
pares = impares = []
for c in range(1, 8):
    numeros.append(int(input(f'Digite o {c} Valor: ')))
    lista_numeros.append(numeros[:])
    numeros.clear()
for sub_lista in lista_numeros:
        
    if sub_lista[0] % 2 == 0:
        pares.append(sub_lista)
    else:
        impares.append(sub_lista)
lista_numeros.append([pares, impares])
print(lista_numeros)