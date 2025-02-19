frase = str(input('Digite sua frase: ')).strip().lower()
palavras = frase.split()
frase_semesp = ''.join(palavras)
invertido = frase_semesp[::-1]
if frase_semesp == invertido:
    print('A frase: "{}" é palindromo'.format(frase))
else:
    print('A frase: "{}", não é palindromo'.format(frase))

