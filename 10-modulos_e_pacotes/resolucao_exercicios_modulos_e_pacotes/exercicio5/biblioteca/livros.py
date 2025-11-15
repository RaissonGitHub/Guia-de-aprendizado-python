# Exercicio 5:
livros = []  # cada livro pode ser um dicionário: {"titulo": ..., "autor": ...}

def adicionar_livro(titulo, autor):
    livro = {"titulo": titulo, "autor": autor}
    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")
