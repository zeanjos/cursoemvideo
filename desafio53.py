
for c in range(1, 4):
    frase = str(input(f'Digite sua {c}ª Frase: ')).strip().lower()
    pal = frase.split()#palavras
    frasejunta = ''.join(pal)#frase sem espaço
    invertido = frasejunta[::-1]
    if invertido == frasejunta:
        print(f'Essa {c}ª frase digitada é palíndromo.')
    else:
        print('Essa frase digitada não é palíndromo.')