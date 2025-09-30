lista_de_salarios = []
contador = 0
while contador < 5:
    salario = float(input("Digite o salário do funcionário aqui: " ))
    contador += 1
    if contador == 5:
        for salario in lista_de_salarios:
            if salario < 2800:
                aumento = salario * (20/10)
                aumento_salarial = salario + aumento
                print(f"Novo salário do funcionário: {aumento_salarial}")
            if salario > 2800 and salario <= 7000:
                aumento = salario * (15/100)
                aumento_salarial = salario + aumento
                print(f"Novo salário do funcionário: {aumento_salarial}")
            if salario > 7000 and salario <= 15000:
                aumento = salario * (10/100)
                aumento_salarial = salario + aumento
                print(f"Novo salário do funcionário: {aumento_salarial}")
            if salario > 15000:
                aumento = salario * (5/100)
                aumento_salarial = salario + aumento
                print(f"Novo salário do funcionário: {aumento_salarial}")