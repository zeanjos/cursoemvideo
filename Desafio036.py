valcasa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o seu salário: '))
anos = float(input('Em quantos anos você irá pagar? '))
ano = anos*12
passou = sal * 0.30
total = valcasa / ano
if total <= passou:
    print('Você poderá prosseguir com o emprestimo pois o seu salário R${:.2f}\n Fica acima do esperado para o emprestimo, a parcela fica de: R${:.2f}'.format(sal, total))
else:
    print('Você não poderá prosseguir com o emprestimo pois o seu salário R${:.2f}\n Fica abaixo do esperado para o emprestimo, a parcela fica de R${:.2f}'.format(sal, total))
