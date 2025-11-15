# Exercicio 5:
def relatorio_final(*args_notas, **kwargs_info):
   """Calcula a média de notas e lista as informações do aluno."""
  
   # 1. Calcular média das notas (args)
   if args_notas:
       media = sum(args_notas) / len(args_notas)
       print(f"Média das notas: {media:.2f}")
   else:
       print("Nenhuma nota fornecida.")


   print("Detalhes do Aluno:")
  
   # 3. Iterar sobre as informações (kwargs)
   if kwargs_info:
       for chave, valor in kwargs_info.items():
           print(f"  {chave.capitalize()}: {valor}")
   else:
       print("  Nenhuma informação adicional fornecida.")


# Exemplo de chamada
relatorio_final(8.5, 9.0, 7.0, nome="Ana", turma="Python B", status="Aprovada")
