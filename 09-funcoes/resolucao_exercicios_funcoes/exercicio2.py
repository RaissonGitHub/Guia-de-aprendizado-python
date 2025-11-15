# Exercício 2:
def detalhes_produto(nome, preco, categoria):
   """Exibe os detalhes formatados de um produto."""
   print(f"Produto: {nome}, Categoria: {categoria}, Preço: R${preco}")


# 1. Chamada com argumentos posicionais
detalhes_produto("Notebook", 3500.00, "Eletrônicos")


# 2. Chamada com argumentos nomeados (em ordem diferente)
detalhes_produto(preco=199.90, nome="Teclado Mecânico", categoria="Periféricos")
