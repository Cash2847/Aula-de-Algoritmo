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
for dias, vendas in vendas_por_dia_do_mes.values():
    if vendas > media_de_vendas:
        Dias_Acima_da_Media[dias] = vendas


print(f"As vendas por dia foram {vendas_por_dia_do_mes}")
print(f"O total de vendas foram {soma_de_vendas}")
print("O dia do com mais vendas no mês teve ", mais_vendas,"vendas.")
print("O dia com menos vendas no mês teve ", menos_vendas,"vendas.")
print("A média de vendas por dia no mês foi de ", media_de_vendas,".")
print("Os dias que possuem um número de vendas acima da média são ", Dias_Acima_da_Media,".")

