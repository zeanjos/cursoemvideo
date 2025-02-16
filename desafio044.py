print('{:^40}'.format('Loja do seu Zé!'))
valor = float(input('Digite o valor do produto R$: '))
escolha = int(input("""Formas de pagamento: 
1- PIX
2 - dinheiro
3- à vista no cartão
4- parcelando 2x no cartão sem juros!
5- 3x ou mais no cartão com 20% de juros? 
\nDigite: """))
while escolha > 5:
    print('\nVocê digitou um número incorreto, digite novamente uma das opções!\n')
    escolha = int(input("""Formas de pagamento: 
1- PIX
2 - dinheiro
3- à vista no cartão
4- parcelando 2x no cartão sem juros!
5- 3x ou mais no cartão com 20% de juros? 
\nDigite: """))
pix = valor - (valor*0.20)
if escolha == 1:
    print('\nO desconto foi de 20% O valor deste produto pagando com pix, valor ficou de: R${}'.format(pix))
elif escolha == 2:
    dinheiro = valor - (valor*0.10)
    print('\nO desconto foi de 10% de desconto pagando à vista no dinheiro, valor ficou de: R${}'.format(dinheiro))
elif escolha == 3:
    cartao = valor - (valor*0.05)
    print('\nO desconto foi de 5% de desconto pagando à vista no cartão, valor ficou de R${}'.format(cartao))
elif escolha == 4:
    valorf = valor / 2
    print('\nParcelando em 2x no cartão o valor sai o mesmo, sem acrescimo, sem descontos, em duas parcelas fica R${} .'.format(valorf))
elif escolha == 5:
    parcelas = int(input('\nDigite a quantidade de parcelas: '))
    while parcelas < 3:
        print('\n O valor digitado é menor que 3 parcelas, digite novamente.\n')
        parcelas = int(input('\nDigite a quantidade de parcelas: '))
    valorjuros = valor + (valor * 0.20)
    valorjuroscorreto = valorjuros / parcelas
    print('\nO valor das parcelas será de R${:.2f} em {} Vezes, o valor total com juros é de: R${:.2f}.'.format(valorjuroscorreto, parcelas, valorjuros))
    
