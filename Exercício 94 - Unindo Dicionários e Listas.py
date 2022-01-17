pessoas = []
soma_idades = []

while True:
    pessoa = {
        'Nome': str(input('Informe o nome: ')),
        'Idade': int(input('Informe a idade: '))
        }

    while True:
        pessoa['Sexo'] = str(input('Informe o sexo [M/F]: ')).lower().strip()[0]
        if pessoa['Sexo'] not in 'mf':
            print('Erro! Por favor, digite apenas M ou F.')
        else:
            break

    soma_idades.append(pessoa['Idade'])

    pessoas.append(pessoa.copy())
    pessoa.clear()

    opcao = str(input('Deseja continuar [N/S]? ')).lower().strip()[0]

    if opcao in 'n':
        break

    while opcao not in 'sn':
        print('Erro! Reponda apenas S ou N.')
        opcao = str(input('Deseja continuar [N/S]? ')).lower()

idade_media = sum(soma_idades)/len(pessoas)

print('-='*18)

print(f'{len(pessoas)} pessoas foram cadastradas.',
      f'\nA Média das idades é de {idade_media:.2f} anos.',
      f'\nAs mulheres cadastradas foram ', end='')

for m in range(len(pessoas)):
    if pessoas[m]['Sexo'] == 'f':
        print(pessoas[m]["Nome"], end=' ')
        
print('.', f'\nLista das pessoas com idade acima da média:')

for p in pessoas:
    if p['Idade'] > idade_media:
        print(f'nome = {p["Nome"]}; sexo = {p["Sexo"]}; idade = {p["Idade"]};')
