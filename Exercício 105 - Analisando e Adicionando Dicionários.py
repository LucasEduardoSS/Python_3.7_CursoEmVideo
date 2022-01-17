def notas(*nota, sit=False):
    """
    -> Função que recebe notas de alunos e informa a maior, menor, media, e opcionalmente a situação do aluno.
    :param nota: Recebe uma ou várias notas.
    :param sit: Opção que mostra a situação das notas do aluno.
    :return: Retorna um dicionário com as informações
    """
    retorno = {'Total': 0, 'Maior': 0, 'Menor': 0, 'Media': 0}
    valores = [*nota]
    media = sum(valores)/len(valores)
    retorno['Maior'] = max(valores)
    retorno['Menor'] = min(valores)
    retorno['Media'] = media
    retorno['Total'] = len(valores)

    if sit:
        if media <= 3:
            retorno['Situação'] = 'Ruim'
        elif media <= 6:
            retorno['Situação'] = 'Média'
        else:
            retorno['Situação'] = 'Boa'

    return retorno

# Programa Principal
res = notas(3, 5, 9, 10, sit=True)
print(res)

# Solução do Professor

def notas(*n, sit=False):
    """
    -> Função que recebe notas de alunos e informa a maior, menor, media, e opcionalmente a situação do aluno.
    :param n: Recebe uma ou várias notas.
    :param sit: Opção que mostra a situação das notas do aluno.
    :return: Retorna um dicionário com as informações
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)

    if sit:
        if r['Media'] <= 3:
            r['Situação'] = 'Ruim'
        elif r['Media'] <= 6:
            r['Situação'] = 'Média'
        else:
            r['Situação'] = 'Boa'

    return r

# Programa Principal
res = notas(3, 5, 9, 10, sit=True)
print(res)
