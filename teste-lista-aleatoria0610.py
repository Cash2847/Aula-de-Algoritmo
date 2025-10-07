import random
import time
import tracemalloc

# lista randomica de inteiros (1-10) com 1000 elementos
# Avaliar o tempo de execução
tracemalloc.start()

inicio = time.time()

memoria_atual, memoria_pico = tracemalloc.get_tracemalloc_memory

lista = [random.randint(1, 100) for i in range(1000)]
print(lista)

final = time.time()


print(f"O tempo de execução é: {final-inicio:.3f} segudos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")

tracemalloc.stop()