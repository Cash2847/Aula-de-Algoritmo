
minha_lista = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print(f"Lista original: {minha_lista}")

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
