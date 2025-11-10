import tracemalloc
import time
import random

tracemalloc.start()
inicio = time.time()


minha_lista = [random.randint(0, 100) for i in range(0, 20)]
print(f"Lista original: {minha_lista}")


n = len(minha_lista)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if minha_lista[j] < minha_lista[min_index]:
            min_index = j
    valor_minimo = minha_lista.pop(min_index)
    minha_lista.insert(i, valor_minimo)

print(f"Lista ordenada: {minha_lista}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")
