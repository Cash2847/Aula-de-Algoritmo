import random
import tracemalloc
import time

tracemalloc.start()
inicio = time.time()

minha_lista = [random.randint(0, 100) for i in range(0, 100)]
print(f"Lista original: {minha_lista}")


def bubble_sort(minha_lista):
    for numero in range(len(minha_lista)-1, 0, -1): 
        for i in range(numero):
            if minha_lista[i] > minha_lista[i+1]: 
        
                temp = minha_lista[i]
                minha_lista[i] = minha_lista[i+1]
                minha_lista[i+1] = temp
    return minha_lista


lista_organizada = bubble_sort(minha_lista)
print(f"\nLista ordenada: { bubble_sort(minha_lista)}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"\nO tempo de execução é: {final-inicio:.3f} segundos.")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB.")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB.")
