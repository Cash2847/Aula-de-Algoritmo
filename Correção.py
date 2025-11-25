

# Implemente um programa para um museu de artes, visando atender tanto aos visitantes,
# interessados em explorar as obras (presencialmente ou virtualmente), quanto aos
# colaboradores, responsáveis pela gestão e manutenção do acervo. O museu abriga uma
# variedade de obras de arte, representando artistas de diferentes períodos e estilos. Cada
# obra possui informações detalhadas, como título, data de criação, tema, estilo artístico,
# descrição, técnica utilizada, autor e localização na sala de exposição. Os artistas, por sua
# vez, têm seus próprios perfis cadastrados, contendo nome, data e local de nascimento,
# biografia e os estilos artísticos aos quais estão associados. Os estilos artísticos são
# caracterizados por uma denominação, período de influência, descrição das características
# predominantes e a principal escola representativa do estilo. Além disso, as obras de arte
# podem ser acompanhadas por documentos relacionados, como cartas, fotografias ou
# entrevistas. Em algumas ocasiões, uma obra retrata uma figura proeminente da época,
# como nobres ou militares, sendo realizada uma pesquisa sobre a pessoa retratada e
# cadastrada como parte das informações da obra. O museu também realiza empréstimos
# de obras para eventos externos, registrando informações como período de empréstimo,
# nome do evento, responsável e tema. Esse registro é essencial para manter o histórico dos
# empréstimos e acompanhar as obras temporariamente fora do museu. Além disso, turistas
# e escolas frequentemente solicitam visitas guiadas com roteiros específicos. Esses
# roteiros incluem um tema, descrição e as obras a serem visitadas em sequência.

# No programa é preciso conter
# 1. Funções
# 2. Utilização de listas
# 3. Utilização de dicionários
# 4. A utilização de um Algoritmo de Ordenação, ficando a seu critério a escolha
# 5. Implemente um algoritmo de Busca
# 6. Uso de Arquivos (podendo ser leitura ou escrita)
# 7. Deve considerar possíveis exceções


with open("Obras do Museu.txt", 'w') as obras:
    obras = {
    'Torre Destruída' : {
        'Data de Criação': 1525, 
        'Tema': "Arrogância da Humanidade", 
        'Descrição': "A arte mostra uma torre imensa, com o seu topo destuído e desgastado. Essa torre representa a arrogância da humanidade,"
        "obsecada em subir aos céus e alcançar os deuses", 
        'Técnica Utilizada': "Pintor começou com pinceladas que, vistas de primeira, parecem aleatórias, até a imagem desejada ser formada.", 
        'Artista' : {
            'Nome': "Giovanni Monneti",
            'Data de Nascimento': 1489,
            'Local de Nascimento' : "Lôndres, Inglaterra",
            'Estílo Artístico' : {
                'Denominação' : "Arte borrada", 
                'Período de Influência': 1500, 
                'Descrição das Características Predominantes': "Pintor começou com pinceladas que, vistas de primeira, "
                "parecem aleatórias, até a imagem desejada ser formada.",
                }        },
        'Localização na Sala de Exposição': "Bloco 3",
        'Preço de Empréstimo': 3860
        },
        
    'Humano Ascendente' : {
        'Data de Criação': 1872, 
        'Tema': "Estado de Iluminação", 
        'Estilo Artístico': "Pintura com marca de mão",
        'Descrição': "A pintura demonstra um humano que atingiu o estado de iluminação e harmonia.", 
        'Técnica Utilizada': "O artita pinta a prórpia mão com a cor desejada e marcando a tela até chegar na imagem que deseja.", 
        'Artista' : {
            'Nome': "Elizabeth Maltinez",
            'Data de Nascimento': 1825,
            'Local de Nascimento' : "Tokyo, Japão",
            'Estílo Artístico' : {
                'Denominação' : "Pintura com marca de mão", 
                'Período de Influência': 1850, 
                'Descrição das Características Predominantes': "O artita pinta a prórpia mão com a cor desejada e marcando a tela até"
                "chegar na imagem que deseja.",
                }
                    }, 
        'Localização na Sala de Exposição': "Bloco 1",
        'Preço de Empréstimo': 2500
        },

    'Leviathan' : {
        'Data de Criação': 1400, 
        'Tema': "Monstro Bíblico", 
        'Estilo Artístico': "Imagem de Mil Palavras",
        'Descrição': "A arte apresenta a imagem de uma criatura bíblica colossal chamada de Leviathan.", 
        'Técnica Utilizada': "O artista escreveun o nome da entidade diversas vezes, criando a imagem da criatura "
        "quando as palavras foram conectadas.", 
        'Artista' : {
            'Nome': "Gabriel Souza",
            'Data de Nascimento': 1350,
            'Local de Nascimento' : "Rio de Janeiro, Brasil",
            'Estílo Artístico' : {
                'Denominação' : "Imagem de Mil Palavras", 
                'Período de Influência': 1370, 
                'Descrição das Características Predominantes': "O artista escreve o nome da entidade diversas vezes, criando a"
                "imagem da criatura quando as palavras foram conectadas.",
                }
                    }, 
        'Localização na Sala de Exposição': "Bloco 4",
        'Preço de Empréstimo': 4000
        },

    'Fênix de Mil Pedaços' : {
        'Data de Criação': 2010, 
        'Tema': "A Ave que Renasce das Cinzas", 
        'Estilo Artístico': "Uso de materiais descartáveis.",
        'Descrição': "O artista utiliza vários materiais considerados como descartáveis ou recicláveis"
                "posicionando-os em ângulos específicos para cria uma ilusão de ótica onde o olho humano enxerga todos os diversos materias"
                "como um único objeto.",
        'Técnica Utilizada': "", 
        'Artista' : {
            'Nome': "Arthur Wilson",
            'Data de Nascimento': 1972,
            'Local de Nascimento' : "Florida, Estados Unidos",
            'Estílo Artístico' : {
                'Denominação' : "Uso de materiais descartáveis", 
                'Período de Influência': 2000, 
                'Descrição das Características Predominantes': "O artista utiliza vários materiais considerados como descartáveis ou recicláveis"
                "posicionando-os em ângulos específicos para cria uma ilusão de ótica onde o olho humano enxerga todos os diversos materias"
                "como um único objeto.",
                }
                    }, 
        'Localização na Sala de Exposição': "Bloco 2",
        'Preço de Empréstimo': 4200
        }
        }

Blocos = [obras['Fênix de Mil Pedaços']['Localização na Sala de Exposição'], obras['Humano Ascendente']['Localização na Sala de Exposição'], obras['Leviathan']['Localização na Sala de Exposição'], obras['Torre Destruída']['Localização na Sala de Exposição']]
print(f"Lista de Blocos da Sala de Exposição: {Blocos}")

blocos_ordenados = sorted(Blocos)
print(f"Lista de Blocos Ordenada: {blocos_ordenados}")

def busca_artes(obras):
        if obra_escolhida == 'Torre Destruída':
            print(f"\nTítulo: {obra_escolhida}.")
            print(f"\nData de Criação: {obras[obra_escolhida]['Data de Criação']}.")
            print(f"\nTema: {obras[obra_escolhida]['Tema']}.")
            print(f"\nDescrição: {obras[obra_escolhida]['Descrição']}.")
            print(f"\nLocalização: {obras[obra_escolhida]['Localização na Sala de Exposição']}")
        
        if obra_escolhida == 'Humano Ascendente':
            print(f"\nTítulo: {obra_escolhida}.")
            print(f"\nData de Criação: {obras[obra_escolhida]['Data de Criação']}.")
            print(f"\nTema: {obras[obra_escolhida]['Tema']}.")
            print(f"\nDescrição: {obras[obra_escolhida]['Descrição']}.")
            print(f"\nLocalização: {obras[obra_escolhida]['Localização na Sala de Exposição']}")
        
        if obra_escolhida == 'Leviathan':
            print(f"\nTítulo: {obra_escolhida}.")
            print(f"\nData de Criação: {obras[obra_escolhida]['Data de Criação']}.")
            print(f"\nTema: {obras[obra_escolhida]['Tema']}.")
            print(f"\nDescrição: {obras[obra_escolhida]['Descrição']}.")
            print(f"\nLocalização: {obras[obra_escolhida]['Localização na Sala de Exposição']}")

        if obra_escolhida == 'Fênix de Mil Pedaços':
            print(f"\nTítulo: {obra_escolhida}.")
            print(f"\nData de Criação: {obras[obra_escolhida]['Data de Criação']}.")
            print(f"\nTema: {obras[obra_escolhida]['Tema']}.")
            print(f"\nDescrição: {obras[obra_escolhida]['Descrição']}.")
            print(f"\nLocalização: {obras[obra_escolhida]['Localização na Sala de Exposição']}")
        if obra_escolhida not in obras:
            raise Exception("\nEssa obra não faz parte do museu.")

try:
    obra_escolhida = input("\nDigite aqui o nome da obra que gostaria de ver sobre: ")
    busca_artes(obras)
except Exception as erro:
    print(erro)