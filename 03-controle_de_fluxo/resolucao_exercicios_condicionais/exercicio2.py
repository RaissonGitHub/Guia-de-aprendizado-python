"""Determina o resultado de tentar abrir um baú com uma chave."""

chave = input("Digite a chave que você possui: ")

if chave == "ouro":
    print("Tesouro encontrado!")
elif chave == "prata" or chave == "bronze":
    print("Tente novamente")
else:
    print("Chave inválida")