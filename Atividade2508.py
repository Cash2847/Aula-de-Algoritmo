# lista = ["Arroz", "Feijão", 3, 4]
# lista.append("Elemento")
# print(lista)
# print(lista[0], lista[4])
# lista[0] = "Macarrão"
# print(lista)
# lista.insert(2, "Batata")
# lista.insert(3, "Banana")
# lista.insert(1, "Carne")
# print(lista)

# Quantidade = len(lista)
# print(Quantidade, "componentes")

# for i in lista:
#     print(i)

# for i in range(len(lista)):
#     print(i, ":", lista[i])

# Lista_2 = [5, 6, 7]

# lista.extend(Lista_2)
# print(lista)

# lista.remove("Macarrão")
# print(lista)

# lista.pop(0) #Remove o índice
# print(lista)

# # del lista (Deleta a lista completamente)
# # print(lista)

# Lista_3 = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(Lista_3):
#     print(Lista_3[i])
#     i += 1

#Estudo de Caso 1 – Temperaturas da Semana
#Enunciado:

#Crie um programa que:

#    1. Receba as temperaturas de 7 dias e armazene em uma lista.
#    2. Mostre a média das temperaturas da semana.
#    3. Informe o dia mais quente e o dia mais frio.
#    4. Mostre quantos dias ficaram acima da média.

Temperaturas_da_Semana = [45, 32, 27, 34, 54, 12, 50]
Média_das_Temperatuas = sum(Temperaturas_da_Semana)/ len(Temperaturas_da_Semana)
Dia_Quente = max(Temperaturas_da_Semana)
Dia_Frio = min(Temperaturas_da_Semana)

print("A média das temperaturas da semana é: ", Média_das_Temperatuas)
print("O dia mais quente da semana foi: ", Dia_Quente)
print("O dia mais frio da semana foi: ", Dia_Frio)
for i in Temperaturas_da_Semana:
    if i > Média_das_Temperatuas:
        print(i)

# Estudo de Caso 2 – Lista de compras interativa

# Enunciado:

# Faça um programa que:

#    1. Permita ao usuário adicionar itens a uma lista de compras.
#    2. Caso o usuário digite "sair", o programa encerra.
#    3. Mostre a lista final de compras organizada em ordem alfabética.

Lista_de_Itens = ["Arroz", "Celular", "Refrigerante", "Anél"]

Lista_de_Itens.append(input("O que você gostaria de adcionar á lista? "))
Lista_de_Itens.append(input("O que mais você gostaria de adicionar? "))

Lista_de_Itens.sort()

print(Lista_de_Itens)

# Estudo de Caso 3 – Analisando números pares e ímpares
# Enunciado:

# Escreva um programa que:

#    1. Receba 10 números inteiros digitados pelo usuário.
#    2. Separe-os em duas listas: pares e ímpares.
#    3. Exiba quantos números pares e ímpares foram digitados.

Lista_de_Números = []
Quantidade_de_Números_em_Lista = 0

while True:
    Escolha_Números = Lista_de_Números.append(input("Quais números você gostaria de adicionar? "))
    Quantidade_de_Números_em_Lista += 1

    if Quantidade_de_Números_em_Lista < 10:
        Escolha_Números = Lista_de_Números.append(input("Quais números você gostaria de adicionar? "))
    else:
        
    

#Estudo de Caso 4 - Controle de Vendas em uma Loja de Eletrônicos

#Contexto do Problema

#Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro
#diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu
#para criar um programa simples em Python para armazenar, analisar e gerar pequenos
#relatórios sobre as vendas do dia.

#O sistema precisa:
#    1. Guardar os produtos vendidos (nome e preço).
#    2. Mostrar o valor total arrecadado.
#    3. Identificar o produto mais caro e o mais barato do dia.
#    4. Permitir consultar se um produto específico foi vendido.

