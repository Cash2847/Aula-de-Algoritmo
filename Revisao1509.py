# Problema 1 – Restaurante Inteligente
# Um restaurante armazena os pedidos do dia em uma lista de dicionários, onde cada pedido tem:
# cliente, itens (lista de dicionários com prato e preco).

# Tarefas:
# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).
# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.



pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    },
    {
     "cliente": "Bruno",
        "itens": [
            {"prato": "Pizza", "preço": 40},
            {"prato": "Refrigerante", "preço": 6},
            {"prato": "Sobremesa", "preço": 12}
        ]   
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preço": 40},
            {"prato": "Suco de Laranja", "preço": 8}
        ]
    }
]

def valor_de_gastos(cliente):
    valor_total_gasto = 0
    for pedido in pedidos:
        if pedido["cliente"] == cliente:
            for item in pedido["itens"]:
                valor_total_gasto += (item["preco"])
    return valor_total_gasto
        

print(valor_de_gastos("Ana"))

def prato_mais_vendido():
    contagem = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            if prato not in contagem:
                contagem[prato] = 0
            contagem[prato] +=1

    quantidade_vendida = 0
    for prato, qtd in contagem.items():
        if qtd > quantidade_vendida:
            quantidade_vendida = qtd
            mais_vendido = prato
    return mais_vendido
print("total: ", prato_mais_vendido())

# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

def ranking_de_clientes():
    gasto = {}
    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = sum(item["preço"] for item in pedido["itens"])
        gasto[cliente]  = total
        var = sorted(gasto.items(), key = lambda x: x[1], reverse=True)[:3]
    print(var) 


atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga": 10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos": {"Corrida": 20, "Ciclismo": 18}
    },
]

def media_de_idade(atletas, esporte_procurado):
    soma_idades = 0
    contagem_atletas = 0
    for atleta in atletas:
        if esporte_procurado in atleta["modalidades"]:
            soma_idades += atleta["idade"]
            contagem_atletas += 1
    if contagem_atletas > 0:
        return soma_idades / contagem_atletas
    else:
        return 0
    
media_de_esporte = media_de_idade(atletas, "Natação")
print(f"Média de idade dos atletas de natação: {media_de_esporte}")
    
def esporte_mais_treinado(dados_atleta):
    if not dados_atleta["treinos"]:
        return "Nenhum treino registrado"
    
    esporte_mais = max(dados_atleta["treinos"], key=dados_atleta["treinos"].get)
    return esporte_mais

def atletas_mais_de_duas_modalidades(dados_atletas):
    nomes_atletas = []
    for atleta in dados_atletas:
        if len(atleta["modalidades"]) > 2:
            nomes_atletas.append(atleta["nome"])
    return nomes_atletas

atleta_escolhido = {"nome": "Lucas", "idade": 20, "modalidades": ["Natação", "Corrida"], "treinos": {"Basquetebol": 12, "Atletismo": 8}}
esporte = esporte_mais_treinado(atleta_escolhido)
print(f"O esporte mais treinado por {atleta_escolhido['nome']} foi: {esporte}") 

ranking_de_clientes()


# Problema 3 – Loja de Música Online com Estatísticas
# Uma loja virtual armazena músicas em uma lista de dicionários, cada música com:
# titulo, artista, downloads, avaliacoes (lista de notas de 1 a 5).
# Tarefas:
# 1. Crie uma função que calcule a nota média de avaliação de cada música.
# 2. Crie uma função que mostre qual artista tem o maior número total de downloads
# somando todas as suas músicas.
# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das
# notas).

musicas = [
    {
        "Título": "Back in Black",
        "Artista": "AC/DC",
        "Downloads": 6800,
        "Avaliações": [5, 4, 5, 5, 4, 5]
    },
    {
        "Título": "Stairway to Heaven",
        "Artista": "Led Zeppelin",
        "Downloads": 8900,
        "Avaliações": [5, 5, 4, 5, 5, 5]
    },
    {   
        "Título": "Enter Sandman",
        "Artista": "Metallica",
        "Downloads": 8100,
        "Avaliações": [5, 5, 5, 4, 4, 5, 5,]
    }
]



# Problema 4 – Ranking de Filmes
# Você recebeu uma lista de filmes (cada filme é um dicionário) com os campos:
# • titulo → nome do filme
# • diretor → nome do diretor
# • bilheteria → valor em milhões de dólares
# • avaliacoes → lista de notas de 1 a 10
# Tarefas:
# 1. Top 3 maiores bilheterias
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior
# bilheteria.
# 2. Top 3 melhores avaliados
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de
# cada filme e retorne os 3 melhores.
# 3. Bilheteria por diretor
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes.
# 4. Campeão absoluto
# o Crie uma função campeao(filmes) que mostre qual filme é a melhor combinação
# de bilheteria alta e avaliação média alta.
