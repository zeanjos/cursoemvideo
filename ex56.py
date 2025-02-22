maior = 0
menor = 0
soma = 0
menorfem = 0
name = ''
nmenor = ''
contfem = 0
for n in range(1, 5):
    print('==={}ª Pessoa==='.format(n))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('SexO [M/F]: ')).lower()
    soma += idade
    if n == 1 and sexo in 'Mm':
        maior = idade
        menor = idade
        name = nome
        nmenor = nome
    else:
        if sexo in 'Mm' and idade > maior:
            maior = idade
            name = nome
        if idade < menor:
            menor = idade
            nmenor = nome
        if sexo in 'Ff' and idade < 20:
            menorfem += 1
        if sexo in 'Ff':
            contfem += 1
if contfem == 0:
    print('Não possui nenhuma mulher!')
else:
    print('Possui {} Mulheres.'.format(menor))
media = soma /n
print('Ao todo são {} Mulheres menores que 20 anos.'.format(menorfem))
print('Menor idade e nome: {}, {} Maior idade e nome: {}, {}, a média das idades é: {:.2f}'.format(nmenor, menor, maior, name, media))

