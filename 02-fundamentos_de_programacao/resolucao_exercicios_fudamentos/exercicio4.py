# Exercício 4:

produto = input("Digite o nome do produto: ")
preco_str = input("Digite o preço do produto (ex: 10.50): ")
quantidade_str = input("Digite a quantidade comprada: ")

preco = float(preco_str)
quantidade = int(quantidade_str)

total = preco * quantidade

print("Você comprou", quantidade, "x", produto)
print("Total da compra: R$", total)
