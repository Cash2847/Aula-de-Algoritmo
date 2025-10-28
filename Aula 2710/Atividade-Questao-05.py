#5.Simulação de transações: Crie um programa que simule uma transferência bancária. Peça ao usuário o saldo
#da conta e o valor da transferência. Caso o saldo seja insuficiente, levante uma exceção do tipo 
#ValueError com a mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o usuário.


def saldo_transferencia(saldo_conta, valor_tranferencia):
    if valor_tranferencia > saldo_conta:
        raise ValueError("Saldo insuficiente.")
    else:
        saldo_conta -= valor_tranferencia
        print(f"Seu saldo atual é: {saldo_conta}.")
try:
    saldo_conta = int(input("Digite o saldo de sua conta: "))
    valor_tranferencia = int(input("Digite o valor da transferência: "))
    saldo_transferencia(saldo_conta, valor_tranferencia)

except ValueError as erro:
    print(erro)

finally:
    print("Operação concluída com sucesso.")