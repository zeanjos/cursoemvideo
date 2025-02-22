maior = 0
menor = 0
soma = 0
for n in range(1, 4):
    print('==={}ª Pessoa==='.format(n))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('SexO [M/F]: '))
    soma += idade
    if n == 1:
        maior = idade
        menor = idade
        name = nome
        nmenor = nome
    else:
        if idade > maior:
            maior = idade
            name = nome
        if idade < menor:
            menor = idade
            nmenor = nome
media = soma /n
print('Menor idade e nome: {}, {} Maior idade e nome: {}, {}, a média das idades é: {:.2f}'.format(nmenor, menor, maior, name, media))