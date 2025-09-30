# 2. Escreva um programa em Python que contenha uma função chamada
# calcula_bonificacao.
#
#  (A). Essa função deve receber dois parâmetros:
# 
# i. taxa_bonus: A porcentagem de bonificação de produção
# concedida ao funcionário.
# 
# ii. salario_base: O salário do funcionário antes da bonificação.
# A função deve calcular e retornar o novo salário do funcionário, já
# incluindo a bonificação. No programa principal, solicite ao usuário que
# informe o salário base e a taxa de bonificação, chame a função e exiba o
# salário final, a bonificação concedida e o salário base informado.

salario_base = float(input("Qual é o salário atual do funcionário? " ))
taxa_bonus = float(input("Qual é a porcentagem de bonificação de produção concedida ao funcionário? " ))
def calcula_bonificacao(salario_base, taxa_bonus):
    aumento = salario_base * (taxa_bonus/100)
    novo_salario = salario_base + aumento
    return novo_salario

print(f"O salario base do funcionário é {salario_base}")
print(f"A taxa de bonus do funcionário é {taxa_bonus}")
print(f"O salario base do funcionário é {calcula_bonificacao(salario_base, taxa_bonus)}")
