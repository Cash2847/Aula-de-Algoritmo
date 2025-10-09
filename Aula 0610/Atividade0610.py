import random
import time
import tracemalloc

lista = [random.randint(1, 100) for i in range(1000000)]



# Método Sequencial 01:

tracemalloc.start()

inicio = time.time()


def buscaSequencial(lista, chave):
    indice = 0
    for numero in lista:
        if numero == chave:
            return indice
        indice = indice + 1
    return -1

resultado = buscaSequencial(lista, 10)
print(resultado)

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")

# Método Sequencial 02:

# def buscaSequencial(lista, chave):
#     n = len(lista)
#     for indice in range(n):
#         if lista[indice] == chave:
#            return indice
#     return -1

# resultado = buscaSequencial(lista, 20)
# print(resultado)

# # Método Sequencial 03

# def buscaSequencial(lista, chave):
#     for (índice, número) in enumerate(lista):
#         if número == chave:
#             return índice
#     return -1

# resultado = buscaSequencial(lista, 40)
# print(resultado)

# for i in range(len(lista)):
#     print(i, lista[i])

# for indice, elemento in enumerate(lista):
#     print(f"{indice}: {elemento}")

# Busca Binária

# Método Binário:

tracemalloc.start()

inicio = time.time()

lista.sort()

def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        if lista[pos_meio] < chave:
            pos_ini = pos_meio + 1
    return -1

resultado = buscaBinaria(lista, 10)
print(resultado)

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")

#TAREFA 02:

#Nível 01 – Fundamentos

# 1. Busca Linear Simples

# Dado um vetor de números inteiros e um número alvo, 
# use busca sequencial para verificar se o número está presente.

# Extra: informe o índice se encontrar.

# 2. Contar Ocorrências (Busca Linear)
# Conte quantas vezes um número aparece na lista usando busca sequencial.

# 3. Maior Número (Busca Linear)
# Use busca sequencial para encontrar o maior número em uma lista.

# 4. Menor Número (Busca Linear)
# Similar ao anterior, mas encontre o menor valor.

# 5. Verificar Elemento (Busca Binária)
# Dada uma lista ordenada, implemente a busca binária para verificar se o elemento existe.

lista = [10, 20, 30, 40, 50, 40, 40, 20, 2220]

# for i in range(20):
#     lista.append(i)

def buscaSequencial(lista, chave):
    for (indice, numero) in enumerate(lista):
        if numero == chave:
            return indice
        aparicoes_numero = 0
        for numero in lista:
            aparicoes_numero += 1
            print(f"Esse número apareceu {aparicoes_numero} vezes.")
    return -1
    

resultado = buscaSequencial(lista, 40)
print(resultado)

# Nível 02 – Aplicações Práticas

# 6. Busca de Nome em Lista
# Peça ao usuário para digitar nomes e depois procure um nome específico usando busca linear.

# 7. Busca Binária Recursiva
# Implemente a versão recursiva da busca binária em uma lista ordenada.

# 8. Comparar Tempo de Execução
# Compare o tempo de execução da busca linear e busca binária em uma lista
# com 1 milhão de elementos. Use o módulo time.

# 9. Encontrar Primeira Ocorrência (Busca Binária Modificada)
# Dada uma lista ordenada com elementos repetidos, use busca binária modificada
# para encontrar o índice da primeira ocorrência de um número.

# 10. Localizar Intervalo de Índices

#Nível 03 - Desafios
