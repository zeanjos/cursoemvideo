palavras = ("batata", "abobora", "berinjela", "repolho")

for p in palavras:
    print(f"\nNa palavra {p.upper()} Temos as vogais: ", end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print((letra), end=', ')
    