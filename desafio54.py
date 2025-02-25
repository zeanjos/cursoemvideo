
from datetime import datetime
cm = 0 #contmenor
cmaior = 0
hojes = datetime.now()#hoje sem formatação
hojef_str = hojes.strftime('%Y')#formatando a data
hoje = int(hojef_str)
for c in range(1, 8):
    nascimentosf =  str(input('Digite o ano de seu nascimento: ')).strip()#sem formatação
    nascimento = int(nascimentosf)#nascimento com formatação
    data = hoje - nascimento
    
    if data < 21:
        cm += 1
    if data >= 21:
        cmaior += 1
        
print(f'{cm} Pessoas são menores que 21 anos e {cmaior} são maiores que 18 anos.')




