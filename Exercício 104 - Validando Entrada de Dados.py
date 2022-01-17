def leiaint(texto):
    x = 0
    while True:
        try:
            print(texto, end='')
            x = int(input())
            break
        except TypeError:
            print('Valor inválido, tente novamente!')
        except ValueError:
            print('Valor inválido, tente novamente!')
    return x


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
