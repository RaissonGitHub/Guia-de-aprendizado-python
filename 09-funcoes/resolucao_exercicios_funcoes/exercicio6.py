# Exercicio 6:

# Variável global
total_vendas = 0


def registrar_venda(valor_venda):
   """Adiciona um valor ao total global de vendas."""
   global total_vendas  # Avisa que estamos usando a variável global
   total_vendas += valor_venda
   print(f"Venda de R${valor_venda} registrada.")


# Fazendo as chamadas
registrar_venda(100)
registrar_venda(50)
registrar_venda(200)


# Imprimindo o valor final da variável global
print(f"Total de vendas acumulado: R${total_vendas}")
