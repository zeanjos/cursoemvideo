maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'{c}ª pessoa digite o seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maio peso lido é: {:.2f} Kgs, e o menor peso lido é: {:.2f} Kgs'.format(maior, menor))
        
    
