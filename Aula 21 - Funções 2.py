# Função com parâmtros opcionais
def somar(a=0, b=0, c=0):  # Atribuindo um valor às variáveis parâmetros
    s = a + b + c
    print(f'A soma vale {s}')


somar(5, 3)


# Dependendo da necessidade pode-se preferir definir um retorno possibilitando modifica-lo para vários usos

# * Função sem retorno
def ex_funcao_sem_retorno(a=0, b=0, c=0):
    s = a + b + c
    print(f'Retorno da função: {s}')


# * Função com retorno
def ex_funcao_com_retorno(a=0, b=0, c=0):
    s = a + b + c
    return s


ex_funcao_sem_retorno(4, 5)
print(f'Dobro do retorno da função: {2 * ex_funcao_com_retorno(4, 5)}')
