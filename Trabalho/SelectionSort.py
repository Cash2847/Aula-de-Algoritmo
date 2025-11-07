import tracemalloc

# mylist = [64, 34, 25, 5, 22, 11, 90, 12]

# n = len(mylist)
# for i in range(n-1):
#   min_index = i
#   for j in range(i+1, n):
#      if mylist[j] < mylist[min_index]:
#        min_index = j
#   min_value = mylist.pop(min_index)
#   mylist.insert(i, min_value)

# print(mylist)

tracemalloc.start()

minha_lista = [12, 5434, 65, 23, 12, 342, 10, 3223]


print(minha_lista)

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"A memória atual é: {memoria_atual/1024:.3f} KB")
print(f"A memória em seu pico é: {memoria_pico/1024:.3f} KB")

