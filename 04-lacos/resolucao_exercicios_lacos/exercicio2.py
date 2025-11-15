while True:
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    if a < b:
        print(f"Soma de {a} e {b}: {a+b}")
    else:
        print("Programa finalizado")
        break