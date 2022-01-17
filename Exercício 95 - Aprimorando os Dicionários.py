def tracado(a):
    print('-='*a)


gols = []
jogadores = []

while True:
    # Define o jogador e suas variáveis
    jogador = {'Nome': str(input('Nome do Jogador: ')), 'Gols': 0, 'Total': 0}
    # Recebe a quantidade de partidas que o jogador jogou
    qnt_part = int(input('Quantidade de partidas que ele jogou: '))

    for i in range(qnt_part):
        # Recebe a quantidade de gols que o jogador fez na partida
        gols.append(int(input(f'Quantos gols ele fez na partida {i + 1}: ')))
        # Conta o total de gols que o jogador marcou
        jogador['Total'] += gols[i]

    # atribui à chave Gols a lista de gols do jogador
    jogador['Gols'] = gols

    # Copia o dicionário do jogador atual para lista de jogadores
    jogadores.append(jogador.copy())

    # Recebe a decisão do usuário sobre a continuidade dos registros
    opcao = str(input('Deseja continuar [N/S]? ')).lower().strip()[0]

    # Corrige erro de digitação na opção acima
    while opcao not in 'sn':
        print('Erro! Reponda apenas S ou N.')
        opcao = str(input('Deseja continuar [N/S]? ')).lower().strip()[0]

    if opcao == 'n':
        break

tracado(20), print(jogador), tracado(20)

# Imprime o cabeçalho da tabela
print(f'{"Cod":3} {"Nome":15} {"Gols":15} {"Total":5}'), print('-'*45)

# Imprime a tabela da jogadaores
for p, j in enumerate(jogadores):
    print(f'{p:3} {j["Nome"]:15} {str(j["Gols"]):15} {j["Total"]}')

print('-'*45)
# Recebe de qual jogador o usuário deseja ver as estatísticas
d = int(input('Mostrar dados de qual jogador? (999 para parar) '))

while d != 999 and d <= (len(jogadores) - 1):
    tracado(20)
    # Imprime as estatísticas do jogador
    print(f'--LEVANTAMENTO DO JOGADOR {jogadores[d]["Nome"]}')

    # Imprime os gols marcados pelo jogador em suas partidas
    for pos, j in enumerate(jogadores[d]["Gols"]):
        print(f'No jogo {pos} fez {j} gols.')

    # Oferece ao usuário a opção de ver as estatíscas de outro jogador
    tracado(20)
    d = int(input('Mostrar dados de qual jogador? (999 para parar) '))
