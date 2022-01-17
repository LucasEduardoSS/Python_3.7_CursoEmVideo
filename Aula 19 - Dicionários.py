# Dicionários e suas propriedades

game = {'name': 'Destiny 2', 'developer': 'Bungie', 'release year': 2017}
game_2 = dict['name': 'Destiny 2', 'developer': 'Bungie', 'release year': 2017]

print(game.values())
print(game.keys())
print(game.items())

game['Awards'] = 'Best Community Support'
print(game)

# Para copiar um dicionário deve-se utilizar a função copy, caso contrário, se criará um laço entre as variáveis
# fazendo com que uma eventual modificação ocorra em ambas.
game_copia = game.copy()
print(game_copia)
