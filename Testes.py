### DIFERENÇA ENTRE LISTAS E DICIONÁRIOS ###

lista = []
Dicionario = {
     "Chave" : 10,
     "Outra coisa" : 11
     }

print(Dicionario["Outra coisa"])

#Aluno -> Nome, curso. idade

Aluno = {
     "Nome": "Fulano",
     "Curso" : "Engenharia de Software",
      "Idade" : 26
}

print(Aluno.get("Curso"))

Personagens = {

    "Personagem_1" : {
        "ID": 1,
        "Name": "Rick",
        "Status": "Alive",
        "Species" : "Human"
    },

    "Personagem_2" : {
        "ID": 2,
        "Name": "Morty",
        "Status": "Alive",
        "Species" : "Human"
    }
}

# Personagens.update({"Status" : "Dead"})
# Personagens["Status"] = "Alive"
# Personagens["ID"] = 2
# Personagens.pop("Status")
print(Personagens)



