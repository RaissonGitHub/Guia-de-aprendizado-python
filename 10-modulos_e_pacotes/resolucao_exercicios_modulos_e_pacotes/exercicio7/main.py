# Exercicio 7:
import conversor

print("=== Conversor Binário -> Decimal ===")
num_bin = input("Digite um número binário (ex: 1011): ")

try:
    decimal = conversor.binario_para_decimal(num_bin)
    print(f"O número binário {num_bin} em decimal é: {decimal}")
except ValueError:
    print("Entrada inválida! Certifique-se de digitar apenas 0 e 1.")


