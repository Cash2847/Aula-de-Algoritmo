# def calcular_media_notas():
#     aluno = input(("Digite o nome do aluno: " ))
#     nota_1 = float(input("Digite a nota do aluno: " ))
#     nota_2 = float(input("Digite a nota do aluno: " ))
#     nota_3 = float(input("Digite a nota do aluno: " ))
#     nota_4 = float(input("Digite a nota do aluno: " ))
#     nota_5 = float(input("Digite a nota do aluno: " ))
#     total_notas = [nota_1, nota_2, nota_3, nota_4, nota_5]
#     for i in total_notas:
#         print(f"As notas do aluno {aluno} são: {total_notas}")
#     for notas in total_notas:
#         soma_notas = sum(total_notas)
#         media_notas = len(total_notas)

#         media = soma_notas / media_notas
#         print(f"A média do aluno {aluno} é {media}")
#         return media


# media = calcular_media_notas()

# if media > 7:
#     print("A média é acima de 7. logo, o aluno está aprovado.")
# else:
#     print("A média não é acima de 7. logo, o aluno está reprovado.")

notas = []
def calcular_media_notas(notas):
    contador = 0
    while contador < 5:
        nota = float(input("Digite a nota do aluno: " ))
        notas.append(nota)
        contador += 1
    else:
        print(f"As notas do aluno são: {notas}")
    for nota in notas:
       soma_notas = sum(notas)
       media_notas = len(notas)

    media = soma_notas / media_notas
    print(f"A média do aluno é {media}")
    return media

calcular_media_notas(notas)