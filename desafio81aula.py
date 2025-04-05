numeros = []
continua = True
while continua:
    num = int(input('Digite um número ou -1 para parar: '))
    if num == -1:
        print('Voce desejou parar.')
        continua = False
    else:
        numeros.append(num)
numeros_digitados = len(numeros)
numeros.sort(reverse = True)
print(f'Foram digitados {numeros_digitados} numeros\nOs numeros em ordem decrescente: {numeros}\n', ('O número cinco foi digitado'if 5 in numeros else 'O número cinco não foi digitado.'))
