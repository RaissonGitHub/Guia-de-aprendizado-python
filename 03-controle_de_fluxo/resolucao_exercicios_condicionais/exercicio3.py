"""Determina a autorização de decolagem com base no status do tempo."""

status_tempo = input("Qual o status do clima? \n(ensolarado, nublado, chuvoso)") #\n equivale a uma quebra de linha
if status_tempo == "ensolarado":
    print("Decolagem autorizada")
elif status_tempo == "nublado":
    print("Aguardar")
elif status_tempo == "chuvoso":
    print("Cancelado")
else:
    print("Status não identificado")
