minha_lista = [64, 34, 25, 5, 22, 11, 90, 12]
print(f"Lista original: {minha_lista}")

n = len(minha_lista)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if minha_lista[j] < minha_lista[min_index]:
       min_index = j
  min_value = minha_lista.pop(min_index)
  minha_lista.insert(i, min_value)

print(f"Lista organizada: {minha_lista}") 
