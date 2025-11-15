# Exercício 3:

idade = int(input("Digite sua idade: "))
resposta_estudante = input("Você é estudante? (s/n): ")

# transforma resposta em valor booleano
estudante = (resposta_estudante == "s")

tem_desconto = (idade < 18) or estudante

print("Tem direito a desconto?", tem_desconto)
