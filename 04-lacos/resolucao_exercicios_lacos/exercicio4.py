palavra_entrada = input('Digite uma palavra: ')
palavra_inicial = palavra_entrada.strip().lower()   #padroniza as letras paraminuscula e tira os espaços em branco do inicio e fim da string

palavra_codificada = palavra_inicial.replace('a', '4')
palavra_codificada = palavra_codificada.replace('e', '3')
palavra_codificada = palavra_codificada.replace('i', '1')
palavra_codificada = palavra_codificada.replace('o', '@')
palavra_codificada = palavra_codificada.replace('u', '9')

print(f"Palavra original: {palavra_entrada}\nPalavra codificada: {palavra_codificada}")
