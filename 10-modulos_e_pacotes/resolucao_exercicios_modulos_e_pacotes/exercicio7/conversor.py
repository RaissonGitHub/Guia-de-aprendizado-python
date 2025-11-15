# Exercicio 7: 

def binario_para_decimal(num_bin):
    """
    num_bin: string representando um número binário, ex: '1011'
    """
    # solução simples usando int base 2
    return int(num_bin, 2)

    # Se quiser uma versão manual:
    # decimal = 0
    # potencia = 0
    # for digito in reversed(num_bin):
    #     decimal += int(digito) * (2 ** potencia)
    #     potencia += 1
    # return decimal
