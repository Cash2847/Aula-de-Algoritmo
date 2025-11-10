import tracemalloc
import time
import random

tracemalloc.start()


minha_lista = [random.randint(0, 100) for i in range(0, 20)]
print(f"Lista original: {minha_lista}")

inicio = time.time()

def heapify(minha_lista, n, i):
    maior_heap = i    
    l = 2 * i + 1    
    r = 2 * i + 2  

    if l < n and minha_lista[l] > minha_lista[maior_heap]:
        maior_heap = l

    if r < n and minha_lista[r] > minha_lista[maior_heap]:
        maior_heap = r

    if maior_heap != i:
        minha_lista[i], minha_lista[maior_heap] = minha_lista[maior_heap], minha_lista[i]
        heapify(minha_lista, n, maior_heap)

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(minha_lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Swap max to end
        heapify(lista, i, 0)
    return minha_lista


lista_ordenada = heap_sort(minha_lista)
print(f"Lista organizada: {lista_ordenada}")

final = time.time()
memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")