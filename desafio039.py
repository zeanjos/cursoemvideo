from datetime import datetime
atual = datetime.now()
atualf = atual.strftime('%d/%m/%y')
dia = int(input('Digite o seu dia de nascimento: '))
mes = int(input('Digite o seu mês de nascimento: '))
ano = int(input('Digite o seu ano de nascimento:'))
datanasc = datetime(ano, mes, dia)
print(datanasc)