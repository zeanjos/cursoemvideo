sexo = str(input('Digite o seu sexo [M/F]: ')).lower()

while sexo != 'm' and sexo != 'f':
    print('Você digitou incorretamente, digite novamente!')
    sexo = str(input('Digite o seu sexo [M/F]: ')).lower()
if sexo == 'm':
    print('Sexo Masculino registrado.')
else:
    print('Sexo Feminino registrado.')