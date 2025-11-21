numeros = [10, 20, 30, 40]
print("Antes:", numeros)

# Método 1: substituir diretamente sabendo o índice
# O valor 30 está no índice 2 (lembre: índices começam em 0)
numeros[2] = 35
print("Após substituir pelo índice:", numeros)

# Método 2: substituir buscando o índice por valor (útil quando você não sabe o índice)
numeros = [10, 20, 30, 40]   # recomeça para demonstrar o outro método
if 30 in numeros:
    idx = numeros.index(30)  # index() retorna o índice da primeira ocorrência
    numeros[idx] = 35
print("Após substituir usando index():", numeros)
