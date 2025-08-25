# 1. Faça um programa que leia dois números e mostre qual é o maior.

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
    

# 2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.

Número = int(input("Digite um número: "))

print("Tabuada do ", Número,":")
for i in range(1, 11): 
    {print(Número," X ",i," = ",Número*i)}

# 3. Crie uma função que verifique se um número é primo.

Número_Escolhido = int(input('Escolha um número: '))

def Cálculo_de_Número_Primo():
    if Número_Escolhido > 1:
        for i in range(2, Número_Escolhido):
            if Número_Escolhido % i == 0:
                print(Número_Escolhido, 'não é um número primo.')
                break
        else:
            print(Número_Escolhido, 'é um número primo.')

Cálculo_de_Número_Primo()

# 4. Desenvolva um programa que leia uma lista de números e mostre a média deles.

Lista_de_Números = [12, 32, 43, 56, 45, 421]

Soma_dos_Números = sum(Lista_de_Números)
Média_dos_Números = Soma_dos_Números / len(Lista_de_Números)
print("A média dos números dados:", Média_dos_Números)

    print(f"O número maior é", resultado)
