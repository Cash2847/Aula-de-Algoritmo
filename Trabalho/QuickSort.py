import random
import tracemalloc

tracemalloc.start()

minha_lista =[random.randint(0, 100) for i in range(0, 20)]

def quicksort(z):
    if(len(z)>1):        
        piv = int(len(z)/2)
        valor = z[piv]
        esquerda = [i for i in z if i < valor]
        meio = [i for i in z if i == valor]
        direita = [i for i in z if i > valor]

        res=quicksort(esquerda) + meio + quicksort(direita)
        return res
    else:
        return z
    
print(minha_lista)
lista_ordenada = quicksort(minha_lista)

print(lista_ordenada)

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")
