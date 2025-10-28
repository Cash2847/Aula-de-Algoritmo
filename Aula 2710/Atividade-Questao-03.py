# 3.Bloco else e finally: Escreva um programa que solicite um número ao usuário. Se o número for 
# maior que 10, exiba uma mensagem dizendo que o número é válido. Utilize o bloco else para imprimir 
# que o programa foi executado com sucesso, e o bloco finally para imprimir "Programa encerrado".

try:
    numero = int(input("Digite um número maior que 10: "))
    if numero > 10:
        print("Número válido!")
    else:
        print("Número inválido.")

except ValueError:
    print("Erro na escolha.")

else:
    print("Programa executado com sucesso.")

finally:
    print( "Programa encerrado.")