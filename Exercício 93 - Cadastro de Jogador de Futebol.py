def tracado(a):
    print('-='*a)


gols = []

# Define o jogador e suas variáveis
jogador = {'Nome': str(input('Nome do Jogador: ')), 'Gols': 0, 'Total': 0}
# Recebe a quantidade de partidas que o jogador jogou
qnt_part = int(input('Quantidade de partidas que ele jogou: '))

for i in range(qnt_part):
    # Recebe a quantidade de gols que o jogador fez na partida
    gols.append(int(input(f'Quantos gols ele fez na partida {i + 1}: ')))
    # Conta o total de gols que o jogador marcou
    jogador['Total'] += gols[i]

jogador['Gols'] = gols
tracado(20), print(jogador), tracado(20)

for o in jogador.items():
    # imprmi a tabela de items
    print(f'O campo {o[0]} tem valor {o[1]}')

print('-='*20)
# imprime na tela a quantidade de partidas que o jogador jogou
print(f'O jogador {jogador["Nome"]} jogou {qnt_part} partidas.')

for a in range(qnt_part):
    # Imprime na tela os gols marcados em cada partida
    print(f'=> Na partida {a + 1}, fez {gols[a]} gols.')

# imprime na tela o total de gols
print(f'Foi um total de {jogador["Total"]} gols.')
