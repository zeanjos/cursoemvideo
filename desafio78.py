from math import inf
num = []
menor = inf
while True:
    
        num.append(int(input('Digite um número: ')))
        for i, v in enumerate(num): # I de indice, V de valor
            if num[-1] == v:
                num.pop[-1]
                if menor > v:
                  menor = v
                print('Você digitou um número que já existe.')
            print(f'Indice {i} valor {v}, menor é {menor}')
        
