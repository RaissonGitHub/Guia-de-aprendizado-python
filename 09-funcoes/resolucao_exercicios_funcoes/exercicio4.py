# Exercicio 4:
def criar_personagem(nome, classe="Aventureiro"):
   """Cria um personagem com uma classe padrão opcional."""
   print(f"Personagem {nome} criado como {classe}!")


# 1. Chamada usando o valor padrão para 'classe'
criar_personagem("Herói")


# 2. Chamada especificando a 'classe'
criar_personagem("Mago", "Feiticeiro")
