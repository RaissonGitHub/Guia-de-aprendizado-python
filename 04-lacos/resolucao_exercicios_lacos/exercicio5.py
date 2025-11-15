quantidade_alunos = int(input("Quantidade de alunos que informarão sua altura: "))

alturas = []

for i in range(quantidade_alunos):
    altura_aluno = int(input("Altura do aluno(em centímetros): "))
    alturas.append(altura_aluno)

if len(alturas) > 0:
    print("Relatório")
    print(f"menor estatura: {min(alturas)} cm\n"
          f"maior estatura:{max(alturas)} cm\n"
          f"média de alturas: {sum(alturas)/len(alturas):.2f} cm")
