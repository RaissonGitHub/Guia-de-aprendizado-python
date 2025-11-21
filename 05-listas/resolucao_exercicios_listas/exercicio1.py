frutas = ["maçã", "banana", "uva", "laranja", "pera", "abacaxi"]
print("Lista inicial:", frutas)
# Saída esperada: ['maçã', 'banana', 'uva', 'laranja', 'pera', 'abacaxi']

# Adicionando uma fruta no final da lista com append()
frutas.append("manga")
print("Após append('manga'):", frutas)
# append() adiciona o elemento sempre ao final

# Inserindo uma fruta em uma posição específica com insert(indice, valor)
# Aqui vamos inserir 'kiwi' no índice 2 (terceira posição)
frutas.insert(2, "kiwi")
print("Após insert(2, 'kiwi'):", frutas)
# insert desloca os elementos a partir do índice informado

# Removendo uma fruta pelo valor com remove()
# remove() elimina a primeira ocorrência do valor especificado
frutas.remove("uva")
print("Após remove('uva'):", frutas)

# Removendo e obtendo o elemento removido com pop(indice)
# Sem argumento, pop() remove o último elemento
removida = frutas.pop()  # remove a última fruta e retorna ela
print("Removida com pop():", removida)
print("Lista final:", frutas)
