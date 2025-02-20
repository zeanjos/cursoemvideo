from datetime import datetime
ano_atual = datetime.now()
hoje = int (ano_atual.strftime('%Y'))

tot = 0
tot_menores = 0
for i in range(1, 8):
    ano = int(input('Em que ano o {} nasceu? '.format(i)))
    idade_ano = hoje - ano
    if idade_ano >= 18:
        tot += 1
        
    else:
        tot_menores += 1
print('{} Pessoas tem mais que dezoito anos.'.format(tot))
print('{} Pessoas tem menos que 18 anos.'.format(tot_menores))