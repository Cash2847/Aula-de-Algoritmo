# QUESTÃO 02: Grade de Notas de Alunos

alunos = int(input("Digite a quantidade de alunos: "))
provas = int(input("Digite a quantidade de notas: "))
notas = []

for aluno in range(alunos):
    nota_por_aluno = []
    for prova in range(provas):
        nota = float(input("Digite a nota desse aluno: "))
        nota_por_aluno.append(nota)
    notas.append(nota_por_aluno)

for i in range(alunos):
    media_aluno = sum(notas[i])/provas

for j in range(provas):
    media_provas = sum(notas[i][j] for i in range(alunos))/alunos

print(f"A média é de cada aluno é: {media_aluno}")
print(f"A média é de cada prova é: {media_provas}")
