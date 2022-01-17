# O comando def denine uma função, a função precisa de um identificador
# e pode receber um confunto de parâmetros
def soma(x, y):
    s = x + y
    return s


print(soma(5, 6))


# * Recursividade com funções *

# Uma função recursiva chama ela mesma ou outra função de forma que se repita instruções, se ela chama ela mesma
# então ele é direta, se não, indireta. Toda função recursiva deve ter um ponto critico que encerra o loop.
def fatorial(n):
    if n == 1:
        return n
    else:
        return n * fatorial(n - 1)


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
