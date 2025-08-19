# 1. Faça um programa que leia dois números e mostre qual é o maior.

X = float(input('Digite um número:' ))

Y = float(input('Digite um número:' ))

Maior_Número = max(X, Y)

print("O maior número é:", Maior_Número)
    

# 2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.



# 3. Crie uma função que verifique se um número é primo.



# 4. Desenvolva um programa que leia uma lista de números e mostre a média deles.

num1 = int(input("digite o número "))
num2 = int(input("digite o número "))

def Cálculo(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return None
        
Cálculo(num1, num2)

resultado = Cálculo(num1, num2)

if resultado == None:
    print("São iguais.")
else:
    print(f"O número maior é", resultado)
