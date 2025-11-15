# Exercicio 2:
def calcular_imposto(valor, taxa):
    """
    valor: valor base (float)
    taxa: taxa em porcentagem (por exemplo, 10 para 10%)
    """
    imposto = valor * (taxa / 100)
    total = valor + imposto
    return imposto, total
