
import tracemalloc
import time
import random

tracemalloc.start()


minha_lista = [random.randint(0, 100) for i in range(0, 100)]
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
print(f"\nLista ordenada: {lista_organizada}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"\nO tempo de execução é: {final-inicio:.3f} segundos.")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB.")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB.")

