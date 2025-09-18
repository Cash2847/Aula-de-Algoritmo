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

ranking_de_clientes()
