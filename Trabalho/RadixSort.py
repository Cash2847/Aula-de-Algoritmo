import tracemalloc
import time
import random

tracemalloc.start() 

inicio = time.time()

minha_lista = [random.randint(0, 100) for i in range(0, 20)]
print(f"Lista original: {minha_lista}")
lista_radix = [[], [], [], [], [], [], [], [], [], []]
valor_maximo = max(minha_lista)
exp = 1

while valor_maximo // exp > 0:

  while len(minha_lista) > 0:
    valor = minha_lista.pop()
    indice_radix = (valor // exp) % 10
    lista_radix[indice_radix].append(valor)

  for bucket in lista_radix:
    while len(bucket) > 0:
      valor = bucket.pop()
      minha_lista.append(valor)

  exp *= 10

print(f"Lista ordenada: {minha_lista}")

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.3f} segundos")
print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")
