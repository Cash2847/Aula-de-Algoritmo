
minha_lista = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Lista original: {minha_lista}")
lista_radix = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(minha_lista)
exp = 1

while maxVal // exp > 0:

  while len(minha_lista) > 0:
    val = minha_lista.pop()
    indice_radix = (val // exp) % 10
    lista_radix[indice_radix].append(val)

  for bucket in lista_radix:
    while len(bucket) > 0:
        val = bucket.pop()
        minha_lista.append(val)

    exp *= 10

print(f"Lista atualizada: {minha_lista}")
