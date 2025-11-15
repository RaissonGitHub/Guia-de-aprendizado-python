# Exercicio 5:
usuarios = []  # cada usuário: {"nome": ..., "matricula": ...}

def registrar_usuario(nome, matricula):
    usuario = {"nome": nome, "matricula": matricula}
    usuarios.append(usuario)
    print(f"Usuário '{nome}' (matrícula {matricula}) registrado com sucesso!")

