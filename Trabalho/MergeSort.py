import tracemalloc
import time
import random

tracemalloc.start()


minha_lista = [random.randint(-100, 100) for i in range(0, 20)]
print(f"Lista original: {minha_lista}")

inicio = time.time()

def merge(esquerda, direita):
  resultado = []
  i = j = 0

  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      resultado.append(esquerda[i])
      i += 1
    else:
      resultado.append(direita[j])
      j += 1

  resultado.extend(esquerda[i:])
  resultado.extend(direita[j:])

  return resultado

def merge_sort(minha_lista):
  step = 1
  length = len(minha_lista)

  while step < length:
    for i in range(0, length, 2 * step):
      left = minha_lista[i:i + step]
      right = minha_lista[i + step:i + 2 * step]
      merged = merge(left, right)
      for j, val in enumerate(merged):
        minha_lista[i + j] = val
    step *= 2

  return minha_lista


lista_organizada = merge_sort(minha_lista)
print(f"Lista ordenada: {lista_organizada}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")
