# Exercicio 1:

import operacoes

print("=== Calculadora Simples ===")
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print("\nResultados:")
print(f"Soma: {operacoes.soma(x, y)}")
print(f"Subtração: {operacoes.subtrair(x, y)}")
print(f"Multiplicação: {operacoes.multiplicar(x, y)}")

resultado_divisao = operacoes.dividir(x, y)
if resultado_divisao is not None:
    print(f"Divisão: {resultado_divisao}")
