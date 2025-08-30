# Caso 1: Controle de Presença em Sala de Aula
# Uma professora precisa registrar a presença dos alunos durante a semana.
# • Cada dia da semana terá uma lista com os nomes dos presentes.
# • No final, ela precisa:

# 1. Saber quais alunos estiveram presentes todos os dias.
# 2. Saber quais alunos faltaram em pelo menos um dia.
# 3. Saber o número total de presenças por aluno.

Dias_da_Semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]
Presenças_Na_Semana = {}


Presenças = {
    "Segunda-Feira": ["Ana", "Bruno", "Carlos"],
    "Terça-Feira": ["Ana", "Bruno"],
    "Quarta-Feira": ["Ana", "Bruno", "Carlos"],
    "Quinta-Feira": ["Ana", "Carlos"],
    "Sexta-Feira": ["Ana", "Bruno", "Carlos"]}


Total_de_Dias_de_Aula = len(Dias_da_Semana)
Alunos_Presentes_Todos_Dias = []
Alunos_que_Faltaram_Algum_Dia = []
Presença_por_Aluno = {}


Todos_os_Alunos = set()
for Dia in Dias_da_Semana:
    for Aluno in Presenças.get(Dia, []):
        Todos_os_Alunos.add(Aluno)

for aluno in Todos_os_Alunos:
    Presença_por_Aluno[aluno] = 0

for Dia in Dias_da_Semana:
    for Aluno in Presenças.get(Dia, []):
        Presença_por_Aluno[Aluno] += 1

for Aluno, total_presencas in Presença_por_Aluno.items():
    if total_presencas == Total_de_Dias_de_Aula:
        Alunos_Presentes_Todos_Dias.append(Aluno)
    else:
        Alunos_que_Faltaram_Algum_Dia.append(aluno)

print(f"Alunos que estavam presentes todos os dias: {Alunos_Presentes_Todos_Dias}")
print(f"Alunos que faltaram pelo menos um dia: {Alunos_que_Faltaram_Algum_Dia}")
print("Total de presenças por aluno:")
for aluno, total_presencas in Presença_por_Aluno.items():
    print(f"- {aluno}: {total_presencas} dias")


# Caso 2: Distâncias em Km

# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

import math

Distancias = []
for D in range(6):
    while True:
        try:
            Distancia = float(input(f"Digite a distância da viagem {D+1} (em Km): "))
            Distancias.append(Distancia)
            break  
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


Soma_das_Distancias = sum(Distancias)


Maior_distancia = max(Distancias)
Menor_distancia = min(Distancias)


Media_das_Distancias = math.ceil(Soma_das_Distancias / len(Distancias))

print(f"Distâncias percorridas foram: {Distancias}")
print(f"Distância total: {Soma_das_Distancias:.2f} Km")
print(f"Maior distância: {Maior_distancia:.2f} Km")
print(f"Menor distância: {Menor_distancia:.2f} Km")
print(f"Média das distâncias (arredondada para cima): {Media_das_Distancias:.2f} Km")


# Caso3: Supermercado – Controle de Estoque
# Um supermercado mantém uma lista de produtos e seus preços.
# • Cada item será representado como [nome, quantidade, preco_unitario].
# • O sistema deve:

# 1. Calcular o valor total em estoque.
# 2. Encontrar o produto de maior valor total (quantidade × preço).
# 3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
# unidades.
# 4. Permitir buscar um produto pelo nome e retornar seus dados.

Lista_de_Produtos = [
    {"Nome": "Margarina", "Quantidade": 20, "Preço unitário": 6.10},
    {"Nome": "Presunto", "Quantidade": 10, "Preço unitário": 5.00},
    {"Nome": "Maçã", "Quantidade": 25, "Preço unitário": 13.00},
    {"Nome": "Batata", "Quantidade": 4, "Preço unitário": 15.30},
    {"Nome": "Refrigerante", "Quantidade": 3, "Preço unitário": 16.00}]

def Valor_Total(Lista_de_Produtos):
    Total_de_Produtos = 0
    for Produto in Lista_de_Produtos:
        Total_de_Produtos += Produto["Quantidade"] * Produto["Preço unitário"]
    return Total_de_Produtos

print(f"O valor total dos produtos é de {Valor_Total(Lista_de_Produtos)} reais.")

def Produto_com_mais_Valor(Lista_de_Produtos):
    if not Lista_de_Produtos:
        return None
    return max(Lista_de_Produtos, key=lambda Produto: Produto["Quantidade"] * Produto["Preço unitário"])

Produto_de_Maior_Valor = Produto_com_mais_Valor(Lista_de_Produtos)
if Produto_de_Maior_Valor:
    Valor_do_Produto = Produto_de_Maior_Valor["Quantidade"] * Produto_de_Maior_Valor["Preço unitário"]
    print("O produto mais valioso do mercado é", Produto_de_Maior_Valor["Nome"], "e seu valor é", Valor_do_Produto)

def Produtos_com_Estoque_Baixo(Lista_de_Produtos, Limite = 5):
    return [Produto["Nome"] for Produto in Lista_de_Produtos if Produto["Quantidade"] < Limite]

print(f"Os produtos cujo estoques estão abaixo de 5 unidades são: {Produtos_com_Estoque_Baixo(Lista_de_Produtos)}.")

def Procurar_Produto(Lista_de_Produtos, Nome_do_Produto):
    for Produto in Lista_de_Produtos:
        if Produto["Nome"] == Nome_do_Produto:
            return Produto
    return None

Buscar_por_Nome = input("Qual produto deseja encontrar? ")
Produto_Escolhido = Procurar_Produto(Lista_de_Produtos, Buscar_por_Nome)
if Produto_Escolhido:
    print(f"As informações do produto '{Buscar_por_Nome}' são: {Produto_Escolhido}")
else:
    print("Esse produto não está na lista.")


# Caso 4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:

# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

import random

Lista_de_Vendas_por_Dia = []

for v in range(30):
    Venda_do_Dia = random.randint(1, 40)
    Lista_de_Vendas_por_Dia.append(Venda_do_Dia)

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


# Caso5: Controle de Participação em um Evento
# Os organizadores de um evento registraram os nomes dos participantes de cada atividade em
# listas separadas.
# • Exemplo:
# o Palestra: ["Ana", "Carlos", "Marina"]
# o Workshop: ["Carlos", "João", "Ana"]
# o Mesa-redonda: ["Marina", "João", "Paula"]
# Eles precisam:

# 1. Saber quem participou de todas as atividades.
# 2. Saber quem participou de apenas uma atividade.
# 3. Gerar uma lista com todos os nomes únicos dos participantes.
# 4. Contar quantos participantes distintos houve no evento.

Palestra = ["Ana", "Carlos", "Marina"]
Workshop = ["Carlos", "João", "Ana", "Marina"]
Mesa_Redonda = ["Marina", "João", "Paula"]
Dança = ["Ana", "João", "Marina"]

Atividade_1 = set(Palestra)
Atividade_2 = set(Workshop)
Atividade_3 = set(Mesa_Redonda)
Atividade_4 = set(Dança)

Participou_de_Todas_Atividades = Atividade_1.intersection(Atividade_2, Atividade_3, Atividade_4)

Participantes = Atividade_1.union(Atividade_2, Atividade_3, Atividade_4)

Participou_de_Apenas_Uma = []
for Participante in Participantes:
    Participacao = 0
    if Participante in Atividade_1:
        Participacao += 1
    elif Participante in Atividade_2:
        Participacao += 1
    elif Participante in Atividade_3:
            Participacao += 1
    elif Participante in Atividade_4:
        Participacao += 1

        if Participacao == 1:
             Participou_de_Apenas_Uma.append(Participante)

Participantes_Distintos = len(Participantes)

print(f"Participou de todas as atividades: {Participou_de_Todas_Atividades}")
print(f"Participou de apenas uma atividade: {Participou_de_Apenas_Uma}")
print(f"LIsta de participantes: {Participantes}")
print(f"Participantes distintos: {Participantes_Distintos}")

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

Livros_Emprestados = [
    ["Dom Casmurro", "Ana", 5], 
    ["1984", "Carlos", 12], 
    ["O Hobbit", "Marina", 3],
    ["O Senhor dos Anéis", "Miguel", 10]]
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
