lista_numeros = []
numeros = []
pares = []
impares = []
for c in range(1, 8):
    numeros.append(int(input(f'Digite o {c} Valor: ')))
    lista_numeros.append(numeros[:])
    numeros.clear()
for sub_lista in lista_numeros: 
    if sub_lista[0] % 2 == 0:
        pares.append(sub_lista[0])
    else:
        impares.append(sub_lista[0])
impares.sort()
pares.sort()
lista_numeros = [pares, impares]

print(f'Números pares {lista_numeros[0]}\n' if len(pares)  > 0 else 'Não foi digitado numeros pares\n', f'Lista impares {lista_numeros[1]}' if len(impares) > 0 else 'Não foi digitado numeros impares.')