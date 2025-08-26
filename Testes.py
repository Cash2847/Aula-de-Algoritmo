Quantidade_de_Numeros_em_Lista = 0

while True:
    Lista_de_Numeros = []
    Numeros_Pares = []
    Numeros_Impares = []
    Escolha_Numeros = Lista_de_Numeros.append(input("Quais números você gostaria de adicionar? "))

    if Quantidade_de_Numeros_em_Lista < 10:
        Escolha_Numeros = Lista_de_Numeros.append(input("Quais números você gostaria de adicionar? "))
    
    for n in Lista_de_Numeros:
        if n % 2 == 0:
            Numeros_Pares.append(n)
            print("Os números páres da lista são: ", Numeros_Pares)

        else:
            Numeros_Impares.append(n)
            print("Os números ímpares da lista são: ", Numeros_Impares)
            break
    

