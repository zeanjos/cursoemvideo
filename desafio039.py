from datetime import datetime
atual = datetime.now()
atualf_str = atual.strftime('%Y')
atualf = int(atualf_str)
ano = int(input('Em qual ano você nasceu? Digite: '))
idade = int(atualf - ano)
dezo = 18
falta = int(dezo - idade)
passou = int(idade - dezo)
if idade == 18:
    print('Você está com a idade exata para se alistar! Você já se alistou?')
elif idade > 18:
    if passou ==1:
        print('Você já possui {} Anos de idade, o prazo de alistamento passou à {} Ano.'.format(idade, passou))
    else:
        print('Você já possui {} Anos de idade, o prazo de alistamento passou à {} Anos'.format(idade, passou))    
elif idade < 18:
    if falta == 1:
        print('Você ainda é menor de 18 anos de idade, deverá aguardar mais {} Ano para se alistar.'.format(falta))
    else:
        print('Você ainda é menor de 18 anos de idade, deverá aguardar mais {} Anos para se alistar.'.format(falta))
