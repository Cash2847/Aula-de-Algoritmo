# Busca Sequencial

# EXEMPLO 01

lista = [100, 20, 300, 1, 3452, 54455, 28928, 43425635, 282, 111111, 444, 565]


def buscaSequencial(lista, chave):
    indice = 0
    for numero in lista:
        if numero == chave:
            return indice
        indice = indice + 1
    return -1

resultado = buscaSequencial(lista, 10)
print(resultado)

# EXEMPLO 02

def buscaSequencial(lista, chave):
    n = len(lista)
    for indice in range(n):
        if lista[indice] == chave:
            return indice
    return -1

resultado = buscaSequencial(lista, 20)
print(resultado)

# EXEMPLO 03

def buscaSequencial(lista, chave):
    for (índice, número) in enumerate(lista):
        if número == chave:
            return índice
    return -1

resultado = buscaSequencial(lista, 40)
print(resultado)

# for i in range(len(lista)):
#     print(i, lista[i])

for indice, elemento in enumerate(lista):
    print(f"{indice}: {elemento}")

# Busca Binária

# EXEMPLO 01:

lista.sort()

def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    print(pos_fim)
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        if lista[pos_meio] < chave:
            pos_ini = pos_meio + 1
    return -1

resultado = buscaBinaria(lista, 20)
print(resultado)