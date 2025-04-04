numeros = []
for c in range(0, 5):
    print('-'*30)
    num = int(input('Digite um valor: '))
    if c == 0 or num > numeros[-1]:
        print('Adicionado ao final da lista.')
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-'*30)
print(f'Os valores digitados em ordem são: {numeros}')
