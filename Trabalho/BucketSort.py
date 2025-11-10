import tracemalloc
import time


tracemalloc.start()
inicio = time.time()

minha_lista = [.22, .32, .43, .21, .20, .23, .25, .44, .20, .6763, .122, .222, .12211, .21222, .1211, .55]
print(f"Lista original: {minha_lista}")

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

lista_organizada = bucket_sort(minha_lista)
print(f"\nLista ordenada: {lista_organizada}")

final = time.time()
memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"\nO tempo de execução é: {final-inicio:.3f} segundos.")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB.")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB.")


