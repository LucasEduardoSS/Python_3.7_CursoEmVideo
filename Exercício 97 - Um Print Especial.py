# Função que faz a impressão de um título
def title(msg, t):
    e = len(msg) + 6
    print(f'{t * e}'), print(f'{msg:^{e}}'), print(f'{t * e}')
    return 0


# Corpo Principal
# Chamada que imprime o título
title("Lucas Eduardo", "-")
