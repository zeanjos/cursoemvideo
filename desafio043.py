peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em centimetros ')) / 100
imc = peso / (altura**2)
if imc <= 18.5:
    print('O seu IMC é de: {:.2f} Você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('O seu IMC é de: {:.2f} Você está no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('O seu IMC é de: {:.2f} Você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Tá gigantesco irmão, emagrece essa banha! Imc: {}'.format(imc))
else:
    print('Vai morrer daqui 3 meses parcero!')
    