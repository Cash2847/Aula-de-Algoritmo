# 4. A empresa TPVFR (Todo Programador Vai Ficar Rico) deseja conceder
# aumento salarial aos seus programadores. O aumento será calculado
# conforme o salário atual do programador, de acordo com as seguintes
# regras:
#
#  (A). Salários até R$ 2800,00: aumento de 20%.
#
#  (B). Salários entre R$ 2800,01 e R$ 7000,00: aumento de 15%.
#
#  (C). Salários entre R$ 7000,01 e R$ 15000,00: aumento de 10%.
#
#  (D). Salários acima de R$ 15000,00: aumento de 5%.
# Escreva um programa que recebe o salário de um programador e calcula
# o salário atualizado com o aumento.

salario_1 = float(input("Digite o salário do funcionário aqui: " ))
salario_2 = float(input("Digite o salário do funcionário aqui: " ))
salario_3 = float(input("Digite o salário do funcionário aqui: " ))
salario_4 = float(input("Digite o salário do funcionário aqui: " ))
salario_5 = float(input("Digite o salário do funcionário aqui: " ))

salarios = [salario_1, salario_2, salario_3, salario_4, salario_5]
for salario in salarios:
    if salario < 2800:
        aumento = salario * (20/100)
        aumento_salarial = salario + aumento
        print(f"Novo salário do funcionário: {aumento_salarial}")
    if salario > 2800 and salario < 7000:
        aumento = salario * (15/100)
        aumento_salarial = salario + aumento
        print(f"Novo salário do funcionário: {aumento_salarial}")
    if salario > 7000 and salario < 15000:
        aumento = salario * (10/100)
        aumento_salarial = salario + aumento
        print(f"Novo salário do funcionário: {aumento_salarial}")
    if salario > 15000:
        aumento = salario * (5/100)
        aumento_salarial = salario + aumento
        print(f"Novo salário do funcionário: {aumento_salarial}")