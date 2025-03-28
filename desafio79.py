from math import inf
num = []
menor = inf
indice = -1
while True:
    novo_num = int(input('Digite um número: '))
    
   
    if novo_num  in num:
        print(f'Valor {novo_num}, já está na lista')
    else:
        num.append(novo_num)
    if len(num) > 0:
        menor = inf
        for c, v in enumerate(num): # C é o indice e o V  valor
            if menor > v:
                menor = v
                indice = c

    desejo = str(input('Deseja continuar [S/N] ? ')).lower().strip()
    if desejo == 's':
        print('Você escolheu continuar!')
    elif desejo == 'n':
        print('Você escolheu parar!')
        break
    else:
        print('Você digitou um caracter incorreto!')
        break
print(f'Menor número: {menor}, no indice {indice}')