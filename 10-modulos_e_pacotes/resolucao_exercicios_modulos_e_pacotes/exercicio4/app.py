# Exercicio 4:
import geometria

def mostrar_menu():
    print("=== Cálculo de Áreas ===")
    print("1 - Área do círculo")
    print("2 - Área do quadrado")
    print("3 - Área do triângulo")
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        r = float(input("Digite o raio do círculo: "))
        area = geometria.area_circulo(r)
        print(f"Área do círculo: {area:.2f}\n")

    elif opcao == "2":
        lado = float(input("Digite o lado do quadrado: "))
        area = geometria.area_quadrado(lado)
        print(f"Área do quadrado: {area:.2f}\n")

    elif opcao == "3":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = geometria.area_triangulo(base, altura)
        print(f"Área do triângulo: {area:.2f}\n")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.\n")
