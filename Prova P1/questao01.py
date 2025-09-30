# 1. Escreva um programa em Python que tenha uma função chamada
# calcular_media_notas. Esta função deve receber uma lista de notas de um aluno
# e calcular a média dessas notas. O programa principal deve:
# 
# (A). Solicitar ao usuário que informe o nome do aluno.
# 
# (B). Solicitar ao usuário que informe as notas do aluno (o número de
# notas pode ser variável, mas o programa deve permitir que o usuário
# adicione pelo menos 5 notas).
# 
# (C). Chamar a função calcular_media_notas passando a lista de notas
# e exibir a média das notas.
# 
# (D). Caso a média seja superior ou igual a 7, exibir que o aluno foi
# aprovado. Caso contrário, exibir que o aluno foi reprovado
10.0
5.2
8.8
8.9
2.3
def calcular_media_notas():
    aluno = input(("Digite o nome do aluno: " ))
    nota_1 = float(input("Digite a nota do aluno: " ))
    nota_2 = float(input("Digite a nota do aluno: " ))
    nota_3 = float(input("Digite a nota do aluno: " ))
    nota_4 = float(input("Digite a nota do aluno: " ))
    nota_5 = float(input("Digite a nota do aluno: " ))
    total_notas = [nota_1, nota_2, nota_3, nota_4, nota_5]
    for i in total_notas:
        print(f"As notas do aluno {aluno} são: {total_notas}")
    for notas in total_notas:
        soma_notas = sum(total_notas)
        media_notas = len(total_notas)

        media = soma_notas / media_notas
        print(f"A média do aluno {aluno} é {media}")
        return media


media = calcular_media_notas()

if media > 7:
    print("A média é acima de 7. logo, o aluno está aprovado.")
else:
    print("A média não é acima de 7. logo, o aluno está reprovado.")