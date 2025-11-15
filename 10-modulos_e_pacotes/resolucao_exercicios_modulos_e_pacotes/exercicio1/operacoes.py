# Exercicio 1:

def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return a / b
