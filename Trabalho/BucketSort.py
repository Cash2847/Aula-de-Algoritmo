# def bucket_sort(arr):
#     # 1. Criar baldes
#     # Assume que a entrada está no intervalo [0, 1) ou é normalizada.
#     # O número de baldes pode ser escolhido com base no tamanho do array.
#     num_baldes = 10
#     baldes = [[] for _ in range(num_baldes)]

#     # 2. Distribuir elementos nos baldes
#     for num in arr:
#         # Calcula o índice do balde
#         indice_balde = int(num * num_baldes)
#         # Garante que o último elemento (que pode ser o máximo) vá para o último balde
#         if indice_balde >= num_baldes:
#             indice_balde = num_baldes - 1
#         baldes[indice_balde].append(num)

#     # 3. Ordenar cada balde
#     for i in range(num_baldes):
#         baldes[i] = sorted(baldes[i])

#     # 4. Concatenar baldes
#     arr_ordenado = []
#     for i in range(num_baldes):
#         arr_ordenado.extend(baldes[i])

#     return arr_ordenado

# # Exemplo de uso:
# lista_desordenada = [10, 43, 66, 454, 74, 3421, 23, 22]
# lista_ordenada = bucket_sort(lista_desordenada)
# print(lista_ordenada)
# # Saída esperada: [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]

# def bucket_sort(arr):
#     # 1. Criar baldes
#     # Assume que a entrada está no intervalo [0, 1) ou é normalizada.
#     # O número de baldes pode ser escolhido com base no tamanho do array.
#     num_baldes = 10
#     baldes = [[] for _ in range(num_baldes)]

#     # 2. Distribuir elementos nos baldes
#     for num in arr:
#         # Calcula o índice do balde
#         indice_balde = int(num * num_baldes)
#         # Garante que o último elemento (que pode ser o máximo) vá para o último balde
#         if indice_balde >= num_baldes:
#             indice_balde = num_baldes - 1
#         baldes[indice_balde].append(num)

#     # 3. Ordenar cada balde
#     for i in range(num_baldes):
#         baldes[i] = sorted(baldes[i])

#     # 4. Concatenar baldes
#     arr_ordenado = []
#     for i in range(num_baldes):
#         arr_ordenado.extend(baldes[i])

#     return arr_ordenado

# # Exemplo de uso:
# lista_desordenada = [10, 43, 66, 454, 74, 3421, 23, 22]
# lista_ordenada = bucket_sort(lista_desordenada)
# print(lista_ordenada)
# # Saída esperada: [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]

# Bucket Sort in Python

# def bucketSort(array):
#     bucket = []

#     # Create empty buckets
#     for i in range(len(array)):
#         bucket.append([])

#     # Insert elements into their respective buckets
#     for j in array:
#         index_b = int(10 * j)
#         bucket[index_b].append(j)

#     # Sort the elements of each bucket
#     for i in range(len(array)):
#         bucket[i] = sorted(bucket[i])

#     # Get the sorted elements
#     k = 0
#     for i in range(len(array)):
#         for j in range(len(bucket[i])):
#             array[k] = bucket[i][j]
#             k += 1
#     return array


# array = [.42, .32, .33, .52, .37, .47, .51]
# print("Sorted Array in descending order is")
# print(bucketSort(array))


def bucket_sort(lista):
    buckets = []
    for i in range(len(lista)):
        buckets.append([])

    for j in lista:
        indice_b = int(10 * j)
        buckets[indice_b].append(j)

    for i in range(len(lista)):
        buckets[i] = sorted(buckets[i])
    
    k = 0
    for i in range(len(lista)):
        for j in range(len(buckets[i])):
            lista[k] = buckets[i][j]
            k += 1
    return lista

lista = [12, 32, 43, 54, 10, 11, 4, 30, 21]
lista_organizada = bucket_sort(lista)
print(f"A lista original é: {lista}")

print(f"\n A lista organizada é {lista_organizada}")
# def bucket_sort(sorting):
#     num_buckets = 10
#     buckets = [[] for i in range (num_buckets)]

#     for numero in sorting:
#         indice_bucket = int(num_buckets * buckets)
#         if indice_bucket >= num_buckets:
#             indice_bucket = num_buckets - 1
#             buckets[indice_bucket].append(numero)
