# funcionarios = {
#     'João': {
#         'salário': 1500.38,
#         'cargo' : 'administrador'
#     },

#     'Luiza': {
#         'salário': 1250.90,
#         'cargo' : 'secretária'
#     },

#     'Matheus': {
#         'salário': 3000.00,
#         'cargo' : 'programador'
#     },
# }

# for funcionario in funcionarios:
#     nome = input("Qual é o nome do funcionário? " )
#     if nome in funcionario:
#         salario = input("Quanto é o salário do funcionário? " )
#         if salario in funcionario['salário']:
#             cargo = input("Qual é o cargo desse funcionário? " )
#         if cargo == funcionario['cargo']:
#             print(f"O funcionário que escolheu é {nome}, seu salário é {salario}, e seu cargo é {cargo}.")
                
#     funcionario_escolhido = input("Digite o nome de um funcionário: " )
#     if funcionario_escolhido in funcionarios:
#         print(funcionarios.setdefault)

# funcionario_escolhido = input("Digite o nome de um funcionário: " )
# if funcionario_escolhido in funcionarios:
#     print(funcionarios.get(funcionario_escolhido))

# x = funcionarios.keys
# print(funcionarios)

lista_funcionarios = {}
informacoes = {"salário", "cargo"}
def escolhendo_funcionarios(lista_funcionarios):
    "funcionario" == input("Qual é o nome do funcionário? " )
    salario = input("Quanto é o salário do funcionário? " )
    cargo = input("Qual é o cargo desse funcionário? " )
    informacoes.update({'salário' : salario})
    informacoes.update({'cargo' : cargo})
    lista_funcionarios["funcionario"] = informacoes
    print(lista_funcionarios)

escolhendo_funcionarios(lista_funcionarios)
