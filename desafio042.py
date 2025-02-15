r1 = int(input('Digite o valor do primeiro segmento: '))
r2 = int(input('Digite o valor do segundo segmento: '))
r3 = int(input('Digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos digitados podem formar um triângulo!')
    if r1 == r2 == r3:
        print('É um triângulo equilátero!')
    elif r1 != r2 and r1 != r3 and r2!= r3:
        print('É um triângulo Escaleno!')
    else:
        print('É um triângulo Isósceles!')
else:
    print('Os segmentos digitados não podem formar um triângulo!')
