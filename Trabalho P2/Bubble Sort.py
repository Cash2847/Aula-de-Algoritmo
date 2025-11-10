import random
import tracemalloc
import time

tracemalloc.start()


minha_lista = [random.randint(0, 100) for i in range(0, 20)]
print(f"Lista original: {minha_lista}")

inicio = time.time()

def bubble_sort(minha_lista):
    for numero in range(len(minha_lista)-1, 0, -1): # Garante que cada item é comparado
        for i in range(numero):
            if minha_lista[i] > minha_lista[i+1]: # Compara o elemento atual com o próximo
        # Troca os elementos se estiverem fora de ordem
                temp = minha_lista[i]
                minha_lista[i] = minha_lista[i+1]
                minha_lista[i+1] = temp
    return minha_lista


lista_organizada = bubble_sort(minha_lista)
print(f"Lista organizada: { bubble_sort(minha_lista)}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")