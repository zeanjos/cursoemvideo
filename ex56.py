maior = 0
menor = 0
for n in range(1, 5):
    print('==={}ª Pessoa==='.format(n))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('SexO [M/F]: '))
    if n == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
            name = nome
        if idade < menor:
            menor = idade
            name = nome
print('Menor:{} Maior: {}'.format(menor, maior))