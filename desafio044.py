valor = float(input('Digite o valor do produto R$: '))
escolha = int(input('Você pagará com: \n 1- PIX\n 2 - dinheiro\n 3- à vista no cartão\n 4- parcelando 2x no cartão\n 5- 3x ou mais no cartão com 20% de juros? '))
pix = valor - (valor*0.20)
if escolha == 1:
    print('O desconto foi de 20% O valor deste produto pagando com pix é de: R${}'.format(pix))
elif escolha == 2:
    dinheiro = valor - (valor*0.10)
    print('O desconto foi de 10% de desconto pagando à vista no dinheiro, valor é de: R${}'.format(dinheiro))
elif escolha == 3:
    cartao = valor - (valor*0.05)
    print('O desconto foi de 5% de desconto pagando à vista no cartão, valor é de R${}')
elif escolha == 4:
    print('Parcelando em 2x no cartão o valor sai o mesmo, sem acrescimo, sem descontos.')
else:
    tresx = valor + (valor*0.20)
    print('O valor pagando em 3x ou mais, acrescenta 20 por cento de juros, o valor é de: R${}'.format(tresx))