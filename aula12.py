nome = str(input('Qual é o seu nome: ')).strip().lower().capitalize()

if nome == 'José':
    print('Que nome bonito!! Tenha um bom dia, {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('O seu nome é bem comum no Brasil, {}'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
     print('Que nome masculino esbelto! {}'.format(nome))
else:
        print('Tenha um bom dia, {}'.format(nome))
