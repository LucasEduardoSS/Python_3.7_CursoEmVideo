# - Pré processamentos -
from time import sleep


# Função que faz a contagem
def contagem(i, f, r):
    if i > f:
        r *= - 1
        f -= 2
    print("-"*30)
    for i in range(i, f + 1, r):
        print(i, end=" ")
        sleep(0.5)
    print("Fim!")
    return 0


# - Corpo Principal -
# Contagems e contagem personalizada
contagem(0, 10, 1), contagem(10, 0, 2)
print("\nAgora é sua de vez de personalizar a contagem.")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
razao = int(input("Razão: "))
contagem(inicio, fim, razao)
