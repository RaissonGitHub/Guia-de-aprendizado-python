# Exercicio 7:
nomes = ["Ana", "Pedro", "Maria", "João", "Beatriz"]


# Ordenando a lista pelo comprimento (len) de cada nome usando lambda
nomes_ordenados_por_tamanho = sorted(nomes, key=lambda nome: len(nome))


print(nomes_ordenados_por_tamanho)
