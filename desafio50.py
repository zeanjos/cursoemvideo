soma = 0
for c in range(0,6):
    num = int(input('Digite um número inteiro, para soma de seus numeros pares:'))
    if num % 2 == 0:
        soma += num
print('Os valores que você digitou, somados dão o valor: {}'.format(soma))