jogadores = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
             'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
             'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
             'Bragantino', 'Athletico-PR', 'Chapecoense', 'Atlético-GO', 'Cuiabá'
)
ultimos4 = jogadores[-4:]
nome = sorted(jogadores)



print('Os cinco primeiros colocados são: ', jogadores[0: 5])
print('='*40)
print(f'Os últimos quatro colocados da tabela são: {ultimos4}')
print('='*40)
print(f'O nome dos Times em ordem alfabética: {nome}')
print('='*40)
print(f'Chapecoense está em {jogadores.index('Chapecoense')+ 1}º Na tabela de colocados.')
print('='*40)