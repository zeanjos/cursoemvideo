lista1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
lista2 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
num = int(input('Digite um número entre 0 e 20: '))
if num in lista1:
    print(f'Voce digitou o número "{num}" Por extenso fica', lista2[num])
else:
    print('Erro, você digitou incorretamente')
