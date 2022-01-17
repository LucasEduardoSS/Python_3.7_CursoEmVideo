from time import sleep


def maior_num(*num):
    maior = 0
    lista_num = num
    for n in lista_num:
        if n == lista_num[0]:
            maior = n
        else:
            if n > maior:
                maior = n
    print('-='*30), print('Analisando os valores passados...')
    for n in lista_num:
        print(n, end=" ")
        sleep(1)
    print(f'Foram informados {len(lista_num)} valores ao todo.'), print(f'O maior valor informado foi {maior}.')


maior_num(4, 5, 6, 8, 10, 5060)
