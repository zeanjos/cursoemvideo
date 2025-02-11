n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if media < 5.0:
    print('Você foi reprovado, sua nota média é: {:.2f}'.format(media))
elif media == 5.0 or media <= 6.9:
    print('Você ficou de recuperação, sua nota média é: {:.2f}'.format(media))
else:
    print('Você passou sua nota média é: {:.2f}'.format(media))