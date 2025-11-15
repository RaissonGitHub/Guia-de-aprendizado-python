# Exercicio 2:
from financeiro.impostos import calcular_imposto

print("=== Cálculo de Imposto ===")
valor = float(input("Digite o valor base (R$): "))
taxa = float(input("Digite a taxa de imposto (%): "))

imposto, total = calcular_imposto(valor, taxa)

print(f"\nImposto calculado: R$ {imposto:.2f}")
print(f"Valor final com imposto: R$ {total:.2f}")
