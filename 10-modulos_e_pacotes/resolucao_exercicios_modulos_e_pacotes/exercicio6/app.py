# Exercicio 6:
import temperatura

print("=== Conversor de Temperatura ===")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    c = float(input("Digite a temperatura em °C: "))
    f = temperatura.celsius_para_fahrenheit(c)
    print(f"{c:.2f} °C equivalem a {f:.2f} °F")

elif opcao == "2":
    f = float(input("Digite a temperatura em °F: "))
    c = temperatura.fahrenheit_para_celsius(f)
    print(f"{f:.2f} °F equivalem a {c:.2f} °C")

else:
    print("Opção inválida.")
