import random

Tabuleiro = [["~" for i in range(5)] for i in range(5)]
tesouro_linha = random.randint(0, 4)
tesouro_coluna = random.randint(0, 4)

print(tesouro_linha)
print(tesouro_coluna)
Tentativas = 7

for tentativa in range(Tentativas):
    print("=== Tabuleiro === ")
    for linha in Tabuleiro:
        print(" ".join(linha))

    print(f"tentativa {tentativa + 1} de {Tentativas}")

    while True:
        try:
            linha = int(input("Escolha a linha (0-4): "))
            if 0 <= linha <= 4:
                break
            print("o numero deve ser entre 0 e 4.")
        except ValueError:
            print("por favor, insira um número válido.")

    while True: 
        try:
            coluna = int(input("Escolha a coluna (0-4): "))  
            if 0 <= coluna <= 4: 
                break
            print("o numero deve ser entre 0 e 4.") 
        except ValueError:
            print("por favor, insira um número válido.") 

    if linha == tesouro_linha and coluna == tesouro_coluna:  
        Tabuleiro[linha][coluna] = "T"  
        print("=== Tabuleiro ===") 
        for linha in Tabuleiro:
            print(" ".join(linha))
        print("Parabéns! Você encontrou o tesouro!") 
        break
    else: 
        Tabuleiro[linha][coluna] = "X"
        if linha < tesouro_linha:
            print("O tesouro está mais para baixo.")
        if linha > tesouro_linha:
            print("O tesouro está mais para cima.")
        if coluna < tesouro_coluna:
            print("O tesouro está mais para a direita.")
        if coluna > tesouro_coluna:
            print("O tesouro está mais para a esquerda.")
        if linha < tesouro_linha and coluna < tesouro_coluna:
            print("O tesouro está mais para baixo e para a direita.")
        if linha > tesouro_linha and coluna < tesouro_coluna:
            print("O tesouro está mais para cima e para a direita.")
        if linha < tesouro_linha and coluna > tesouro_coluna:
            print("O tesouro está mais para baixo e para a esquerda.")

if tentativa == Tentativas - 1:
    print("=== Resultado Final ===")
    for linha in Tabuleiro:
        print(" ".join(linha))
    print(f"Game Over! O tesouro estava em ({tesouro_linha}, {tesouro_coluna})")