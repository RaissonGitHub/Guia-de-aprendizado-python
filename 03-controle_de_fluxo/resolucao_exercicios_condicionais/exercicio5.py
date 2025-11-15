"""Determina a estratégia de ataque baseada na cor e tamanho do dragão."""

cor = input("Digite a cor do dragão: ").lower() #método para string, que normaliza todas as letras para minúsculas
tamanho = int(input("Digite o tamanho do dragão em metros: "))

if cor == "vermelho" and tamanho > 5:
    print("Ataque com fogo")
elif cor == "azul" and tamanho <= 5:
    print("Ataque com água")
elif cor == "verde" or (cor == "vermelho" and tamanho <= 5):
    # condição engloba "verde" de qualquer tamanho E "vermelho" de tamanho <= 5
    print("Ataque com terra")
else:
    print("Fugir")