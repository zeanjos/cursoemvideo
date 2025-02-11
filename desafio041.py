idade = int(input('Digite sua idade para verificar a sua categoria de competição: '))
if idade <= 9:
    print('Você competirá na categoria Mirim!')
elif 10 <= idade <= 14:
    print('Você competirá na categoria Infantil!')
elif 14 <= idade <=19:
    print('Você competirá na categoria Junior!')
elif idade == 20:
    print('Você competirá na categoria Amador!')
else:
    print('Você competirá na categoria Master!')