# 1. Tratamento de exceções básicas: Escreva um programa que peça ao usuário dois números e faça a divisão do 
# primeiro pelo segundo. Se o usuário inserir um valor inválido ou tentar dividir por zero, 
# o programa deve exibir uma mensagem de erro apropriada.

tentativas = 0
def calculo():
    try:
        primeiro_numero = int(input("Valor 1: "))
        segundo_numero = int(input("Valor 2: "))
        resultado = primeiro_numero/segundo_numero    

    except ZeroDivisionError:
        print("Não é possível a divisão por 0.")

    except ValueError:
        print("Digite apenas valores inteiros.")

    else:
        print(f"O resultado dos valores é: {resultado}.")

    finally:
        print("Operação realizada com sucesso.")


while tentativas <= 2:
    calculo()
    tentativas += 1