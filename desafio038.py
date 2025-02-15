pri = float(input('Digite o primeiro número: '))
seg = float(input('Digite o segundo número: '))

if pri == seg:
    print('Os valores são iguais! Não existe valores maiores.')
elif pri > seg: 
    print('O valor {} É maior que o valor {}'.format(pri, seg))
else:
    print('O valor {} É maior que o valor {}'.format(seg, pri))
