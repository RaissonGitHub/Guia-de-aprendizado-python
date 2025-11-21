tupla = (100, 200, 300)
print("Tupla original:", tupla)

lista = list(tupla)  # converte para lista
print("Lista resultante:", lista)

# Agora podemos modificar a lista, por exemplo:
lista.append(400)
print("Lista após append:", lista)

# Se quisermos voltar a tupla:
tupla_nova = tuple(lista)
print("Tupla nova:", tupla_nova)
