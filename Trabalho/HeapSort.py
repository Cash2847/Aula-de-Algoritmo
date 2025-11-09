
def heapify(minha_lista, n, i):
    largest = i    
    l = 2 * i + 1    
    r = 2 * i + 2  

    if l < n and minha_lista[l] > minha_lista[largest]:
        largest = l

    if r < n and minha_lista[r] > minha_lista[largest]:
        largest = r

    if largest != i:
        minha_lista[i], minha_lista[largest] = minha_lista[largest], minha_lista[i]
        heapify(minha_lista, n, largest)

def heapSort(minha_lista):
    n = len(minha_lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(minha_lista, n, i)

    for i in range(n - 1, 0, -1):
        minha_lista[i], minha_lista[0] = minha_lista[0], minha_lista[i]  # Swap max to end
        heapify(minha_lista, i, 0)

minha_lista = [12, 11, 13, 5, 6, 7]
lista_ordenada = heapSort(minha_lista)
print("Sorted array is:", heapSort(minha_lista))
