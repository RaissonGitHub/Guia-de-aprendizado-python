# Exercicio 5:
from biblioteca.livros import adicionar_livro, livros
from biblioteca.usuarios import registrar_usuario, usuarios

print("=== Sistema de Biblioteca ===")

# Cadastro de usuários
registrar_usuario("Ana", "2025001")
registrar_usuario("Bruno", "2025002")

# Cadastro de livros
adicionar_livro("Introdução ao Python", "Guido van Rossum")
adicionar_livro("Algoritmos e Lógica de Programação", "Fulano da Silva")

print("\nUsuários cadastrados:")
for u in usuarios:
    print(f"- {u['nome']} (matrícula {u['matricula']})")

print("\nLivros cadastrados:")
for l in livros:
    print(f"- '{l['titulo']}' - {l['autor']}")
