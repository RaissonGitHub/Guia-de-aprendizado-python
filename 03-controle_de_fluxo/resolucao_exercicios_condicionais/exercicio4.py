import random

"""Simula uma rodada de jogo de adivinhação.
   Gera um número secreto e compara com o palpite."""

numero_secreto = random.randint(1, 10)   # Gerando um número aleatório entre 1 e 10
palpite = int(input("Digite um numero de 1 a 10: "))

if palpite == numero_secreto:
    print("Acertou!")
elif palpite > numero_secreto:
    print("Muito alto")
else:  # palpite < numero_secreto
    print("Muito baixo")

print()   #imprime uma linha vazia
print(f"Número secreto: {numero_secreto}\n"
      f"Palpite: {palpite}\n")