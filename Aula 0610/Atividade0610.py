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