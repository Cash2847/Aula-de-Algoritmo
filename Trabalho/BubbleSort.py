# O Bubble Sort é uma função simples que, quando ordenando uma lista, pega um valor por vez, e o compara com o próximo número na lista.
# Caso seja maior, o valor escolhido irá trocar de lugar com o número comparado e repetira o mesmo com o próximo até encontrar um número
# maior do que o valor escolhido.

# O Bubble Sort realiza essa mesma ação com todos os números da lista mostrada para assim, organiza-la por tamanho. Isso faz com que
# essa função seja relativamente simples em seu funcionamento, e que a estrutura de seu código seja menos
# complexa e extensa em comparação à outras opções. Porém, por esses mesmos motivos, esse método não apenas possui uma desvantagem
# Quando a lista é muito grande, como também irá usar muita memória por comparar a lista de número a número.

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

