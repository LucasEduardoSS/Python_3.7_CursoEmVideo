def vezes(x, y):
    p = x * y
    return p


def cal_area():
    lar = int(input('LARGURA (m): '))
    com = int(input('COMPRIMERO (m): '))
    print(f'A área de um terreno de {com}m por {lar}m é {vezes(com, lar):.2f}m2.')


print(f'{"  Controle de Terrenos  ":=^40}'), print('-' * 40)
cal_area()
