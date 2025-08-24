# 1. Cálculo de Complexidade Simples

#Escreva um algoritmo que conte quantas operações básicas (somas) são executadas para calcular 
#a soma dos números de 1 até n. Exiba o resultado e compare com a fórmula matemática n*(n+1)/2.

def Cálculos(n):
    """
    Calcula a soma dos números de 1 a n, conta as operações de adição e compara com a fórmula matemática.

    Args:
        n (int): O número final da sequência.
    """
    Soma = 0
    Número_de_Operações = 0

    for i in range(1, n + 1):
        Soma += i
        Número_de_Operações += 1 

    Fórmula = n * (n + 1) // 2 

    print(f"Com N sendo = {n}:")
    print(f"A soma calculada é: {Soma}")
    print(f"O número de operações executadas foram: {Número_de_Operações - 1}")
    print(f"A soma calculada através da fórmula é: {Fórmula}")
    
    
    if Soma == Fórmula:
        print("Os resultados da soma e da fórmula são iguais.")
    else:
        print("Houve uma diferença entre a soma iterativa e a fórmula.")

n = int(input("Digite um número:" ))
if n <= 0:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    
else:
    Cálculos(n)

#2. Validação de Login

#Implemente um algoritmo que simule um sistema de login:

#• O usuário tem 3 tentativas para digitar a senha correta (senha123).

#• Caso erre todas, mostre "Acesso bloqueado".

#• Caso acerte, mostre "Bem-vindo!"


Tentativas = 0
while True:
    Escolha = input('Digite a senha:' )
    Tentativas += 1

    if Escolha in ['Senha123']:
        print("Bem-vindo!")
        break

    else:
        print("Senha errada! Tente novamente: ")

    if Tentativas > 3:
        print("Acesso bloqueado.")
        break

#3. Estatísticas de Notas

#   Leia as notas de uma turma e:
#   Calcule a média;
#   Mostre a maior e a menor nota;
#   Exiba o percentual de alunos acima da média.


Nota_1 = float(input("Digite a nota do Aluno A: "))
Nota_2 = float(input("Digite a nota do Aluno B: "))
Nota_3 = float(input("Digite a nota do Aluno C: "))
Nota_4 = float(input("Digite a nota do Aluno D: "))
Media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4
Maior_Nota = max(Nota_1, Nota_2, Nota_3, Nota_4)
Menor_Nota = min(Nota_1, Nota_2, Nota_3, Nota_4)

print(f"A media das notas é {Media:.2f}.")
print(f"A maior nota dentre todas foi:", Maior_Nota, '.')
print(f"A menor nota dentre todas foi:", Menor_Nota, '.')

#4. Busca Linear
#Dada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário.
#Informe a posição em que ele aparece ou diga que não foi encontrado.

Nomes = ["Ana", "Bruno", "Carla", "Anais", "Marcella", "Luíza", "Gabriel"]

def Lista(Nomes):
    Nome_Escolhido = input("Por favor, digite um nome: ")

    if Nome_Escolhido in Nomes:
        Posição_do_Nome =  Nomes.index(Nome_Escolhido)
        print("O nome", {Nome_Escolhido}, "está na lista, e sua posição é", {Posição_do_Nome},)

    else:
        print("Esse nome não está na lista.")

Lista(Nomes)


#5. Verificação de CPF (simplificado)
#Peça ao usuário um número de 11 dígitos e:
#   • Verifique se todos os caracteres são dígitos;
#   • Verifique se o tamanho é válido (11);
#   • Mostre "CPF válido" ou "CPF inválido".
#   (Não precisa calcular os dígitos verificadores ainda — é apenas validação estrutural.)

CPF = input("Digite os 11 digitos de seu CPF: ")
Quantidade_de_Digitos = len(str(CPF))

if CPF.isdigit() and Quantidade_de_Digitos == 11:
    print("CPF válido.")
else:
    print("CPF inválido.")

