from datetime import datetime

pessoa = {'Nome': str(input('Nome: '))}
dn = int(input('Data de nascimento: '))
pessoa['Idade'] = datetime.now().year - dn
pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho: '))

if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Idade de Aposentadoria'] = pessoa['Idade'] + pessoa['Ano de Contratação'] + 35 - datetime.now().year

print('-=' * 20)

for a in pessoa.keys():
    print(f' - {a} tem o valor {pessoa[a]}')
