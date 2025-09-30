# salario_base = float(input("Qual é o salário atual do funcionário? " ))
# taxa_bonus = float(input("Qual é a porcentagem de bonificação de produção concedida ao funcionário? " ))
# def calcula_bonificacao(salario_base, taxa_bonus):
#     aumento = salario_base * (taxa_bonus/100)
#     novo_salario = salario_base + aumento
#     return novo_salario

# print(f"O salario base do funcionário é {salario_base}")
# print(f"A taxa de bonus do funcionário é {taxa_bonus}")
# print(f"O salario base do funcionário é {calcula_bonificacao(salario_base, taxa_bonus)}")


salario_base = float(input("Qual é o salário atual do funcionário? " ))
taxa_bonus = float(input("Qual é a porcentagem de bonificação de produção concedida ao funcionário? " ))
def calcula_bonificacao(salario_base, taxa_bonus):
    aumento = salario_base * (taxa_bonus/100)
    novo_salario = salario_base + aumento
    print(f"O salario base do funcionário é {salario_base}")
    print(f"A taxa de bonus do funcionário é {taxa_bonus}")
    print(f"A bonificação do salário do funcionário é {aumento}")
    print(f"O salario com bonificação do funcionário é {novo_salario}")

calcula_bonificacao(salario_base, taxa_bonus)
# print(f"O salario base do funcionário é {salario_base}")
# print(f"A bonificação do salário do funcionário é {aumento}")
# print(f"A taxa de bonus do funcionário é {taxa_bonus}")
# print(f"O salario com bonificação do funcionário é {novo_salario}")