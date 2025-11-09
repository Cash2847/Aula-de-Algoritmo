import tracemalloc

tracemalloc.start()

minha_lista = [12, 5434, 65, 23, 12, 342, 10, 3223]

n = len(minha_lista)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if minha_lista[j] < minha_lista[min_index]:
            min_index = j
    valor_minimo = minha_lista.pop(min_index)
    minha_lista.insert(i, valor_minimo)

print(minha_lista)

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")

