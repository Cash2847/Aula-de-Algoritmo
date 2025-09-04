# Caso 4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:

# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

Lista_de_Vendas_por_Dia = {""}

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
    "Caso-1" : {
        "Livro" : "Dom Casmurro", 
        "Usuário" : "Ana", 
        "Dias_Emprestados" : 5}, 
    "Caso-2" : {
         "Livro" : "1984", 
        "Usuário" : "Carlos", 
        "Dias_Emprestados" : 12
    }, 
    "Caso-3" : {
        "Livro" : "O Hobbit", 
        "Usuário" : "Marina", 
        "Dias_Emprestados" : 3
    },
    "Caso-4" : {
        "Livro" : "O Senhor dos Anéis",
        "Usuário" : "Miguel",
        "Dias_Emprestados" : 10      
    }
}

Livros_Acima_7_Dias = []

for Emprestimos in Livros_Emprestados:
    if Livros_Emprestados["Caso-1"["Dias_Emprestados"]]["Caso-2"["Dias_Emprestados"]]["Caso-3"["Dias_Emprestados"]["Caso-4"["Dias_Emprestados"]]] > 7:
        
