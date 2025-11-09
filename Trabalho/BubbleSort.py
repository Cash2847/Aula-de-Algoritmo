minha_lista = [10, 32, 54, 11, 5, 33, 66, 323, 5, 12]
print(f"Lista original: {minha_lista}")

def bubble_sort(lista): 
    n = len(lista) 
    for i in range(n):
        for j in range(0, n- i - 1):
                if lista[j] > lista[j + 1] : 
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)

lista_organizada = bubble_sort(minha_lista)

print(f"Lista organizada: {lista_organizada}")
