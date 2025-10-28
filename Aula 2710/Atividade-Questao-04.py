#4.Exceções personalizadas: Escreva uma função que verifica se uma senha possui no mínimo 8 caracteres 
# e pelo menos um número. Se a senha não atender aos requisitos, levante uma 
# exceção com uma mensagem personalizada. Trate a exceção e mostre a mensagem ao usuário.

def analise_senha(senha):
    if len(senha) < 8 and not any(c.isdigit() for c in senha):
        raise Exception("A senha deve ter, no mínimo, 8 caracteres e um número.")
    else: 
        print("Senha válida.")
    
try:
    senha = input("Digite sua senha: ")
    analise_senha(senha)

except Exception as erro:
    print(erro)

finally:
    print("O programa foi realizado com sucesso.")


