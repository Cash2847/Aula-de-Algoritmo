
import tracemalloc
import time
import random

tracemalloc.start()


minha_lista = [12, 43, 656, 23, 12, 11, 545, 66, 77, 9, 100, 33, 22, 44, 66, 564]
print(f"Lista original: {minha_lista}")

inicio = time.time()

def counting_sort(lista):
  max_val = max(lista)
  contagem = [0] * (max_val + 1)

  while len(lista) > 0:
    numero = lista.pop(0)
    contagem[numero] += 1

  for i in range(len(contagem)):
    while contagem[i] > 0:
      lista.append(i)
      contagem[i] -= 1

  return lista


lista_organizada = counting_sort(minha_lista)
print(f"Lista organizada: {lista_organizada}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")

