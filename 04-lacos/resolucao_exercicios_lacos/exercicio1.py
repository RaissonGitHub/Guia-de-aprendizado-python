alturas_ondas = []

for i in range(10):
    altura = float(input(f'Digite a altura da {i+1}° onda: '))
    alturas_ondas.append(altura)

ondas_perigosas = 0    #contagem de ondas acima de 2metros

# Processamento: Usa um loop for para iterar sobre a lista,
for altura in alturas_ondas:
    if altura > 2:
        ondas_perigosas += 1

print(f"{ondas_perigosas} ondas perigosas contabilizadas")