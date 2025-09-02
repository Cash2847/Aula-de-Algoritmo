# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno.

Aluno = {
     "Nome": "José",
     "Curso" : "Engenharia de Software",
      "Idade" : 21
}

print(Aluno["Nome"])

# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".

Aluno["Nota"] = 9.5

# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

Produtos = {"Arroz" : "R$ 15.90", "Feijão" : "R$ 9.50", "Macarrão" : "R$ 4.20"}
for Produto, Valor in Produtos.items():
    print(Produto,":", Valor)

# 4. Dado o dicionário aluno, verifique se existe a chave "curso".

if "Curso" in Aluno:
    print("Está no dicionário Aluno.")
# 5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome e nota. Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.

Turma = {
    "Aluno_1" : {
        "Nome" : "João",
        "Nota" : 7.5
    },

    "Aluno_2" : {
        "Nome" : "Maria", 
        "Nota" : 8.0
}

}


print((Turma["Aluno_1"]["Nome"]), (Turma["Aluno_2"]["Nome"]))


# 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.

Carro = {
    "Marca" : "Volkswagen",
    "Modelo" : "Polo",
    "Ano" : 2016
}
print(Carro)
# a. Adicione ao dicionário do carro a chave 'cor'.

Carro["Cor"] = "Vermelho"
print(Carro)

# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
# valor).

Notas_de_Alunos = {
    "Carlos" : 6.8,
    "Eduardo" : 8.0,
    "Lucia" : 10.0
}

print(Notas_de_Alunos)

# c. Acesse a nota de um dos alunos e exiba.

print(f"Eduardo tirou {Notas_de_Alunos["Eduardo"]}")

# d. Remova um aluno do dicionário de notas.

Notas_de_Alunos.pop("Lucia")
print(Notas_de_Alunos)


### PRA CASA ###

# Estudo de Caso : Cadastro de Produtos
# Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve
# conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e
# manipular essas informações.

# Exemplo:

# produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
# print(f"O produto {produto["nome"]} custa R${produto["preco"]}")


# Estudo de Caso 2: Agenda Telefônica
# Uma agenda pode ser representada como um dicionário em que as chaves são os nomes
# das pessoas e os valores são os números de telefone.

# Exemplo:

# agenda = {"Maria": "99999-1234", "João": "98888-5678"}
# print("Telefone da Maria:", agenda["Maria"])
