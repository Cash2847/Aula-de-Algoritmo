import random
import tracemalloc
import time

tracemalloc.start()


minha_lista = [random.randint(0, 100) for i in range(0, 20)]
print(f"Lista original: {minha_lista}")

inicio = time.time()

def quick_sort(z):
    if(len(z) > 1):        
        piv = int(len(z) / 2)
        valor = z[piv]
        esquerda = [i for i in z if i < valor]
        meio = [i for i in z if i == valor]
        direita = [i for i in z if i > valor]

        resultado = quick_sort(esquerda) + meio + quick_sort(direita)
        return resultado
    else:
        return z
    

lista_ordenada = quick_sort(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")
final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")
