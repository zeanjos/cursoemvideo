soma = 0
contidad = 0    #usado para contar a idade e em seguida verificar a média lá em baixo.
maior = None
menor = None
contfem = 0
for c in range(1, 5):
    print('-=-'*20)
    nome = str(input('Digite o seu nome: ')).strip().title()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: [M/F]:  ')).lower()
    soma += idade
    contidad += 1
    if sexo == 'm':
        if maior is None and menor is None:
            maior = idade
            menor = idade
        else:
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade
    elif sexo == 'f':
        if idade < 20:
            contfem += 1
        
media = soma / contidad
print('-=-'*20)
print(f'''A média do grupo é: {media:.2f}\n
A menor idade Masculina é {menor} Anos,\n
A maior idade Masculina é {maior} Anos,\n
A quantidade de mulheres menor que 20 anos são de {contfem}''')
