# 3. Crie um programa em Python que implemente uma função chamada
# calcula_imposto_renda. A função deve receber um único parâmetro:
# salário: o valor do salário bruto de um indivíduo.
# Curso de Graduação em Engenharia de Software
# Algoritmos
# Com base na tabela de alíquotas abaixo, a função deve calcular e
# retornar o valor do imposto de renda devido:

# Faixa Salarial (R$) Alíquota (%) Dedução (R$) Faixa Salarial (R$)
# Até 2.112,00 Isento 0 Até 2.112,01
# De 2.112,01 a 2.826,65 7,50% 158,4 De 2.112,01 a 2.826,66
# De 2.826,66 a 3.751,05 15% 370,4 De 2.826,66 a 3.751,06
# De 3.751,06 a 4.664,68 22,50% 651,73 De 3.751,06 a 4.664,69
# Acima de 4.664,68 27,50% 884,96 Acima de 4.664,69

# Requisitos:
# • A função deve retornar o valor do imposto de renda a ser pago.
# • O programa deve solicitar ao usuário o salário bruto, chamar a função e
# exibir o imposto devido.

salario_1 = float(input("Digite o salário do funcionário aqui: " ))
salario_2 = float(input("Digite o salário do funcionário aqui: " ))
salario_3 = float(input("Digite o salário do funcionário aqui: " ))
salario_4 = float(input("Digite o salário do funcionário aqui: " ))
salario_5 = float(input("Digite o salário do funcionário aqui: " ))

def calcula_imposto_de_renda():
    total_salarios = [salario_1, salario_2, salario_3, salario_4, salario_5]
    for salario in total_salarios:
        if salario <= 2112.0:
            print("A faixa salarial desse funcionário continua a mesma.")
        if salario > 2112.0 and salario <= 2826.65:
                aumento = salario * (750/100)
                deducao = salario - 158.4
                faixa_salarial = salario + aumento
                nova_faixa_salarial = faixa_salarial - deducao
                print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")
        if salario > 2826.65 and salario <= 3751.05:
            aumento = salario * (1500/100)
            deducao = salario - 370.4
            faixa_salarial = salario + aumento
            nova_faixa_salarial = faixa_salarial - deducao
            print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")
        if salario > 2112.0 and salario <= 2826.65:
            aumento = salario * (2250/100)
            deducao = salario - 651.73
            faixa_salarial = salario + aumento
            nova_faixa_salarial = faixa_salarial - deducao
            print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")
        if salario > 4664.68:
                aumento = salario * (2750/100)
                deducao = salario - 884,96
                faixa_salarial = salario + aumento
                nova_faixa_salarial = faixa_salarial - deducao
                print(f"A nova faixa salarial desse funcionário é: {nova_faixa_salarial}")

calcula_imposto_de_renda()