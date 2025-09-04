# Caso 4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:

# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

import random

Lista_de_Vendas_por_Dia = {}

for v in range(30):
    Venda_do_Dia = random.randint(1, 40)
    Lista_de_Vendas_por_Dia.get(Venda_do_Dia)

Vendas_Totais = sum(Lista_de_Vendas_por_Dia)
Menos_Vendas = min(Lista_de_Vendas_por_Dia)
Mais_Vendas = max(Lista_de_Vendas_por_Dia)
Media_de_Vendas = Vendas_Totais / len(Lista_de_Vendas_por_Dia)

Dias_Acima_da_Media = []
for i, Vendas in enumerate(Lista_de_Vendas_por_Dia):
    if Vendas > Media_de_Vendas:
        Dias_Acima_da_Media.append(i)

print(f"As vendas por dia foram {Lista_de_Vendas_por_Dia}")
print("O dia do com mais vendas no mês teve ", Mais_Vendas,"vendas.")
print("O dia com menos vendas no mês teve ", Menos_Vendas,"vendas.")
print("A média de vendas por dia no mês foi de ", Media_de_Vendas,".")
print("Os dias que possuem um número de vendas acima da média são ", Dias_Acima_da_Media,".")


# Caso6: Sistema de Biblioteca
# Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
# [titulo, usuario, dias_emprestado].
# Exemplo:
# [
#  ["Dom Casmurro", "Ana", 5],
#  ["1984", "Carlos", 12],
#  ["O Hobbit", "Marina", 3]
# ]
# O sistema precisa:

# 1. Listar apenas os livros que estão emprestados há mais de 7 dias.
# 2. Encontrar o livro emprestado há mais tempo.
# 3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
# 4. Calcular a média de dias de empréstimo.

Livros_Emprestados = {
    ["Dom Casmurro", "Ana", 5], 
    ["1984", "Carlos", 12], 
    ["O Hobbit", "Marina", 3],
    ["O Senhor dos Anéis", "Miguel", 10]
}

Mais_Dias = -1
Soma_Dos_Dias = 0
Lista_dos_Usuarios = []
Livros_que_Passaram_de_7_Dias = []
for Livro, Usuario, Dias in Livros_Emprestados:
    if Dias > 7:
        Livros_que_Passaram_de_7_Dias.append(Livro)
    if Dias > Mais_Dias:
        Dias == Mais_Dias
        Emprestado_Mais_Tempo = (f"{Livro} por {Usuario}")
    Lista_dos_Usuarios.append(Usuario)
    Soma_Dos_Dias += Dias
    Media_De_Dias = Soma_Dos_Dias / len(Livros_Emprestados)


print(f"Os livros que estão emprestados há mais de 7 dias são: {Livros_que_Passaram_de_7_Dias}")
print(f"O livro emprestado há mais tempo é {Emprestado_Mais_Tempo}.")
print(f"Os usários com livros emprestados são: {Lista_dos_Usuarios}")
print(f"A média de dias de emprétimo é: {Media_De_Dias}")