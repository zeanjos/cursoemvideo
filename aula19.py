filme = {'titulo': 'Starwars',
         'Genero': 'Ficção Ciêntifica',
         'Idade minima permitida': '14 Anos',
         'ano': '1976'
         }
##for chave in filme:
    ##print(f'{chave}: {filme[chave]}')


print(filme.values())#Aqui irá mostrar apenas os valores dentro do dicionario, por exemplo starwars, 
#é um valor que está dentro do dicionario

print(filme.keys())#Aqui irá mostrar as chaves do dicionario, o primeiro item sempre é a chave, titulo, genero
#São chaves.

print(filme.items())#Aqui irá mostrar a chave e valor, 'titulo', 'Starwars' é a primeira chave e valor declarada.
for k, v in filme.items():
    print(f'{k}: {v}')