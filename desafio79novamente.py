from math import inf
menor = inf
num = []
cont = 0
while cont < 5:
    cont += 1
    num.append(int(input('Digite um número: ')))
    for i, v in enumerate(num[:5]):
    
        if menor > v:
            menor = v
        print(f'O menor valor da lista até agora: {menor} no indice: {i}')