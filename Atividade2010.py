# ATIVIDADE 01:

salas = int(input("Entre com o número de salas: "))
dias = int(input("Entre com o número de dias: "))
Temperaturas = []

for sala in range(salas):
    temperatura_dia = []
    for dia in range(dias):
        temperatura_dia.append(int(input("Digite a temperatura: ")))
    Temperaturas.append(temperatura_dia)

print(Temperaturas)

# sala_1 = [Temperaturas[0][0], Temperaturas[0][1], Temperaturas[0][2]]
# total_temperaturas = sum(sala_1)
# media_temperaturas = len(sala_1)
# media = total_temperaturas/media_temperaturas
# print(f"A média das temperaturas da primeira sala é {media}")

# sala_2 = [Temperaturas[1][0], Temperaturas[1][1], Temperaturas[1][2]]
# total_temperaturas = sum(sala_2)
# media_temperaturas = len(sala_2)
# media = total_temperaturas/media_temperaturas
# print(f"A média das temperaturas da segunda sala é {media}")

# sala_3 = [Temperaturas[2][0], Temperaturas[2][1], Temperaturas[2][2]]
# total_temperaturas = sum(sala_3)
# media_temperaturas = len(sala_3)
# media = total_temperaturas/media_temperaturas
# print(f"A média das temperaturas da terceira sala é {media}")

# sala_4 = [Temperaturas[3][0], Temperaturas[3][1], Temperaturas[3][2]]
# total_temperaturas = sum(sala_4)
# media_temperaturas = len(sala_4)
# media = total_temperaturas/media_temperaturas
# print(f"A média das temperaturas da quarta sala é {media}")

# sala_5 = [Temperaturas[4][0], Temperaturas[4][1], Temperaturas[4][2]]
# total_temperaturas = sum(sala_5)
# media_temperaturas = len(sala_5)
# media = total_temperaturas/media_temperaturas
# print(f"A média das temperaturas da quinta sala é {media}")

for i in salas:
    media = sum(dia)/2
print(media) 

# QUESTÃO 02: