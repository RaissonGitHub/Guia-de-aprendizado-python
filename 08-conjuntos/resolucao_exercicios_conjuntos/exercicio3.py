# Passo 1: receber nomes do usuário.
# Estratégia: pedir que o usuário digite nomes separados por vírgula (ex: Ana, Pedro, Maria)
entrada = input("Digite nomes separados por vírgula (ex: Ana, Pedro, Maria): ")

# Passo 2: transformar a string em lista de nomes e limpar espaços extras
# split(',') separa onde há vírgula; strip() remove espaços no começo/fim
nomes_crus = [nome.strip() for nome in entrada.split(',') if nome.strip() != ""]

# Se o usuário não digitou nada, avisamos e encerramos
if not nomes_crus:
    print("Nenhum nome informado.")
else:
    # Passo 3: usar set para eliminar duplicatas
    # Opcional: normalizar caixa (como lower()) se quiser ignorar diferenças entre 'Ana' e 'ana'
    # Aqui vamos manter a capitalização do usuário, mas eliminar exatamente iguais.
    nomes_unicos = set(nomes_crus)

    # Passo 4: converter de volta para lista e ordenar alfabeticamente
    lista_final = list(nomes_unicos)
    lista_final.sort()  # ordena em ordem alfabética

    # Passo 5: exibir o resultado
    print("Nomes únicos em ordem alfabética:")
    for nome in lista_final:
        print("-", nome)
