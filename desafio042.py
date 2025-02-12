r1 = int(input('Digite o valor do primeiro segmento: '))
r2 = int(input('Digite o valor do segundo segmento: '))
r3 = int(input('Digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r1 == r3 and r2 == r3:
    print('Todos os lados são iguais, um triângulo equilátero!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and (r1 == r2 or r1 == r3 or r2 ==3):
    print('Este triângulo é isosceles, possui dois lados iguais!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and (r1 != r2 and r1 != r3 and r2 != r3):
    print('Este triângulo é escaleno, possui todos os lados diferentes! ')
else:
    print('Não é um triângulo!')
