soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:
    print('Você informou {} numero par, o valor do número é: {}'.format(cont, soma))
elif cont >1:
    print('Você informou {} numeros pares, e a soma dos numeros pares foram: {}'.format(cont, soma))
else:
    print('Você não digitou nenhum numero par!')