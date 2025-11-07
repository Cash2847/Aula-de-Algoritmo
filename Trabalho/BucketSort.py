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

def bucket_sort(sorting):
    num_buckets = 10
    buckets = [[] for _ in range (num_buckets)]
