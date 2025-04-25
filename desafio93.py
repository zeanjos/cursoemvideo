aproveitamento = {}

aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
aproveitamento['partidas'] = int(input(f'Digite quantas partidas "{aproveitamento['nome']}" jogou: ').strip())
for c in range (1, aproveitamento['partidas'] + 1):
    aproveitamento['gols'] = int(input(f'Digite a quantidade de gols feito na {c}ª partida: ').strip())
    aproveitamento[f'jogo{c}']
for k, v in range (aproveitamento.items):
    print(k, v)