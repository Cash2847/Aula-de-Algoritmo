# Problema 1 – Restaurante Inteligente
# Um restaurante armazena os pedidos do dia em uma lista de dicionários, onde cada pedido tem:
# cliente, itens (lista de dicionários com prato e preco).

# Tarefas:
# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).
# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.
# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.


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


# def valor_do_gasto(cliente):
#     valor_total_gasto = 0
#     for pedido in pedidos:
#         cliente_escolhido = valor_do_gasto
#         if cliente_escolhido in pedido["cliente"]:
#             valor_total_gasto += sum(pedido["itens"])
#             print(valor_total_gasto)

# print(f"O clinte gastou aproximadamente {valor_do_gasto(pedidos)}")

def valor_de_gastos(cliente):
    valor_total_gasto = 0
    for pedido in pedidos:
        if pedido["cliente"] == cliente:
            for item in pedido["itens"]:
                valor_total_gasto += (item["preco"])
    return valor_total_gasto
        

print(valor_de_gastos("Ana"))
