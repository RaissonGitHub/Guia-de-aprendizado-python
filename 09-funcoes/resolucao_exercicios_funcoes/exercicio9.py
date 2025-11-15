# Exercicio 9:
import time


def timer(func):
   """Decorador que imprime o tempo de execução e mensagens de início/fim."""
  
   # Função wrapper que recebe os argumentos da função original
   def wrapper(*args, **kwargs):
       # 2. Antes de executar
       print("Iniciando função...")
      
       # 3. Executar a função original
       resultado = func(*args, **kwargs)
      
       # 4. Depois de executar
       print("Função finalizada.")
      
       # 5. Retornar o resultado
       return resultado
      
   # Retorna a função wrapper
   return wrapper


# Aplicando o decorador
@timer
def tarefa_simples():
   """Uma tarefa simples que é decorada."""
   print("Executando tarefa...")
   # Simulando um pequeno trabalho
   time.sleep(0.5)
   return True


# Chamando a função decorada
print("\n--- Chamando a tarefa simples ---")
resultado_tarefa = tarefa_simples()
print(f"Resultado da tarefa: {resultado_tarefa}")
