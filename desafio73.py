times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
             'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
             'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
             'Bragantino', 'Athletico-PR', 'Chapecoense', 'Atlético-GO', 'Cuiabá'
)

ultimos_times = times[-4:]
primeiros_cinco = times[0: 5]
print('-='*20)
print(f'Os cinco primeiros times da tabela do Brasileirão são: {', '.join(primeiros_cinco)}.')
print('-='*20)
print(f'Os quatro últimos times da tabela do Brasileirão são: {', '.join(ultimos_times)}.')
print('-=')
print(f'Os times em ordem alfabética:\n {', '.join(sorted(times))}')
print('-='*20)
print(f'O time da chapecoense está na posição {times.index('Chapecoense') + 1}º.')
print('-='*20)
