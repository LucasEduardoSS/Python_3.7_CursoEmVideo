# Funções importadas
from random import randrange
from time import sleep


# Função que sorteia valores para um lista
def sort_nums(x):
    nums = [randrange(1, 10, 1) for i in range(x)]
    print(f"Sorteando 5 valores da lista: ", end='')
    for n in nums:
        print(n, end=' ')
        sleep(1)
    print('Pronto!')
    print(f'Somando os valores pares de {nums}, temos {soma_list_nums(nums)}.')


# Função que soma os valores de um lista
def soma_list_nums(x):
    soma = 0
    for n in x:
        if n % 2 == 0:
            soma += n
    return soma


# Corpo Principal do Programa
sort_nums(5)
