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
