# salario_1 = float(input("Digite o salário do funcionário aqui: " ))
# salario_2 = float(input("Digite o salário do funcionário aqui: " ))
# salario_3 = float(input("Digite o salário do funcionário aqui: " ))
# salario_4 = float(input("Digite o salário do funcionário aqui: " ))
# salario_5 = float(input("Digite o salário do funcionário aqui: " ))

lista_de_salarios = []
def calcula_imposto_de_renda(lista_de_salarios):
    contador = 0
    while contador < 5:   
        salario = float(input("Digite o salário do funcionário aqui: " ))
        lista_de_salarios.append(salario)
        contador += 1
        for salario in lista_de_salarios:
            if salario <= 2112.0:
                print(f"A faixa salarial desse funcionário continua sendo {salario}.")
            if salario > 2112.0 and salario <= 2826.65:
                aumento = salario * (7.5/100)
                salario = salario + aumento
                deducao = 158.4
                salario = salario - deducao
                print(f"A nova faixa salarial desse funcionário é: {salario}")
            if salario > 2826.65 and salario <= 3751.05:
                aumento = salario * (15/100)
                salario = salario + aumento
                deducao = 370.4
                salario = salario - deducao
                print(f"A nova faixa salarial desse funcionário é: {salario}")
            if salario > 2112.0 and salario <= 2826.65:
                aumento = salario * (22.50/100)
                salario = salario + aumento
                deducao = 651.73
                salario = salario - deducao
                print(f"A nova faixa salarial desse funcionário é: {salario}")
            else:
                aumento = salario * (27.50/100)
                salario = salario + aumento
                deducao = 884.96
                salario = salario - deducao
                print(f"A nova faixa salarial desse funcionário é: {salario}")

calcula_imposto_de_renda(lista_de_salarios)


# def calcula_imposto_de_renda():
#     total_salarios = [salario_1, salario_2, salario_3, salario_4, salario_5]
#     for salario in total_salarios:
#         if salario <= 2112.0:
#             print("A faixa salarial desse funcionário continua a mesma.")
#         if salario > 2112.0 and salario <= 2826.65:
#                 aumento = salario * (750/100)
#                 deducao = salario - 158.4
#                 faixa_salarial = salario + aumento
#                 nova_faixa_salarial = faixa_salarial - deducao
#                 print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")
        # if salario > 2826.65 and salario <= 3751.05:
        #     aumento = salario * (1500/100)
        #     deducao = salario - 370.4
        #     faixa_salarial = salario + aumento
        #     nova_faixa_salarial = faixa_salarial - deducao
        #     print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")
#          if salario > 2112.0 and salario <= 2826.65:
#              aumento = salario * (22.50/100)
#              deducao = salario - 651.73
#              faixa_salarial = salario + aumento
#              nova_faixa_salarial = faixa_salarial - deducao
#              print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")
# #         if salario > 4664.68:
#                 aumento = salario * (2750/100)
#                 deducao = salario - 884,96
#                 faixa_salarial = salario + aumento
#                 nova_faixa_salarial = faixa_salarial - deducao
#                 print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")

# calcula_imposto_de_renda()

# notas = []
# def calcular_media_notas(notas):
#     contador = 0
#     while contador < 5:
#         nota = float(input("Digite a nota do aluno: " ))
#         notas.append(nota)
#         contador += 1
#     else:
#         print(f"As notas do aluno são: {notas}")
#     for nota in notas:
#        soma_notas = sum(notas)
#        media_notas = len(notas)

#     media = soma_notas / media_notas
#     print(f"A média do aluno é {media}")
#     return media

# calcular_media_notas(notas)