# Caso 4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:

# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

import random
import statistics

vendas_por_dia_do_mes = {}  
numero_de_vendas = 30
Dias_Acima_da_Media = {}

for i in range(numero_de_vendas):
    vendas_por_dia = random.randint(1, 40) 
    vendas_por_dia_do_mes[f"Dia_{i+1}"] = vendas_por_dia

vendas_totais = vendas_por_dia_do_mes.values()

soma_de_vendas = sum(vendas_por_dia_do_mes.values())
menos_vendas = min(vendas_por_dia_do_mes.values())
mais_vendas = max(vendas_por_dia_do_mes.values())
media_de_vendas = sum(vendas_totais) / len(vendas_totais)
statistics.mean(vendas_por_dia_do_mes.values())
for vendas in vendas_por_dia_do_mes.values():
    if vendas > media_de_vendas:
        Dias_Acima_da_Media = vendas


print(f"As vendas por dia foram {vendas_por_dia_do_mes}")
print(f"O total de vendas foram {soma_de_vendas}")
print("O dia do com mais vendas no mês teve ", mais_vendas,"vendas.")
print("O dia com menos vendas no mês teve ", menos_vendas,"vendas.")
print("A média de vendas por dia no mês foi de ", media_de_vendas,".")
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

Livros_emprestados = {
    "Dom Casmurro" : {"Usuário": "Ana", "Dias-Emprestados": 5},
    "1984" : {"Usuário": "Carlos", "Dias-Emprestados": 12},
    "O Hobbit" : {"Usuário": "Marina", "Dias-Emprestados": 3},
    "O Senhor dos Anéis": {"Usuário": "Miguel", "Dias-Emprestados": 10},
    "Harry Potter" : {"Usuário": "Diana", "Dias-Emprestados": 8},
}

Livros_antigos = {}
for titulo, dados in Livros_emprestados.items():
    if dados["Dias-Emprestados"] > 7:
        Livros_antigos[titulo] = dados
print(f"Os livros emprestados há mais de 7 dias são: {Livros_antigos}")

Livro_mais_antigo = None
Maximo_de_dias = 0
for titulo, dados in Livros_emprestados.items():
    if dados["Dias-Emprestados"] > Maximo_de_dias:
        Maximo_de_dias = dados["Dias-Emprestados"]
        Livro_mais_antigo = {titulo: dados}
print(f"O livro emprestado há mais tempo é: {Livro_mais_antigo}")

Total_de_dias = 0
Numero_de_emprestimos = len(Livros_emprestados)
for dados in Livros_emprestados.values():
    Total_de_dias += dados["Dias-Emprestados"]

Media_de_dias = Total_de_dias / Numero_de_emprestimos if Numero_de_emprestimos > 0 else 0
print(f"Média de dias é: {Media_de_dias}")
