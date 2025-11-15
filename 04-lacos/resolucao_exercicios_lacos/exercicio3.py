quantidade = 1
total_colhido = 0

while quantidade != 0:
    quantidade = int(input("Insira a quantidade de frutos da árvore: "))
    if quantidade >= 10:
        total_colhido += quantidade

print(f"Total da colheita: {total_colhido}")