# Exercicio 8
def gerar_saudacao_personalizada(prefixo):
   """Função fábrica que cria uma função de saudação."""
  
   # Função interna (Closure)
   def saudar(nome):
       # 'prefixo' é capturado do escopo externo (gerar_saudacao_personalizada)
       return f"{prefixo}, {nome}!"
      
   # Retorna a função interna
   return saudar


# Teste (Closure)
# 1. Criando a função de saudação matinal
saudacao_manha = gerar_saudacao_personalizada("Bom dia")


# 2. Usando a função gerada
print(saudacao_manha("Carlos"))


# Teste extra (provando que o prefixo é lembrado)
saudacao_tarde = gerar_saudacao_personalizada("Boa tarde")
print(saudacao_tarde("Maria"))
