maior = 0
menor = 0
soma = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª Pessoa: '.format(p)))
    soma += peso
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
media = soma / p
print('O maior peso é: {}\n O menor peso é: {}'.format(maior, menor))
print('A média de pesos digitados é: {}'.format(media))
