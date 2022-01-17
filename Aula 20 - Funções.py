# A função de def define uma função
def soma(a, b):  # Pode receber inumeros parãmetros personalizados
    resultado = a + b
    print(resultado)
    return 0


def soma_ind(*num):
    # Tem suas próprias rotinas
    s = 0
    for n in num:
        s += n
    print(s)
    return 0  # Por convenção deve retornar algo


# Quando chamada, recebe atribuições para cada um dos parâmetros
soma(5, 450)
soma_ind(4, 5, 6, 7, 8)
