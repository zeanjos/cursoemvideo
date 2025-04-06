numeros = []
impares = []
pares = []
continua = True
while continua:
    num = int(input('Digite um números, se desejar sair digite -1: '))
    if num < 0:
        print('Voce escolheu sair.')    
        continua = False
    else:
        numeros.append(num)
        if num % 2 == 0:
            pares.append(num)
        elif num % 2 > 0:
            impares.append(num)
contagem_impar = len(impares)
contagem_par = len(pares)
print(f'Os números digitados foram {numeros}\n' ifA lista de pares foi {pares}\nA lista de impares foi {impares}')
