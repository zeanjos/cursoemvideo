aproveitamento = {}
total = 0
aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
aproveitamento['partidas'] = int(input(f'Digite quantas partidas "{aproveitamento['nome']}" jogou: ').strip())
for c in range (1, aproveitamento['partidas'] + 1):
    aproveitamento[f'jogo{c}'] = int(input(f'Digite a quantidade de gols feito na {c}ª Partida: '))
print(f'O jogador {aproveitamento['nome']}, jogou {aproveitamento['partidas']} Partidas')
for c, v in aproveitamento.items():
    if 'jogo' in c:
        print(f'Jogo {c[4:]}: {v}')
        total += v

print(f'Foi um total de {total}')