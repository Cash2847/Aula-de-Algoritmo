minha_lista = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(f"Lista original: {minha_lista}")

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

def merge_sort(arr):
  step = 1
  length = len(arr)

  while step < length:
    for i in range(0, length, 2 * step):
      left = arr[i:i + step]
      right = arr[i + step:i + 2 * step]
      merged = merge(left, right)
      for j, val in enumerate(merged):
        arr[i + j] = val
    step *= 2

  return arr


lista_organizada = merge_sort(minha_lista)
print(f"Lista organizada: {lista_organizada}")
