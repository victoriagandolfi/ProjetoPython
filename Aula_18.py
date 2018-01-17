candidatos = [
    {
        "nome": "Camila Campos",
        "partido": "PMDB",
        "cargo": "prefeita",
        "vice": "Michel Temer",
        "numero": "15",
        "votação": [],
        "percentagem_votos": []
    },
    {
        "nome": "Monica Rezende",
        "partido": "PT",
        "cargo": "prefeita(o)",
        "vice": "Lula",
        "numero": "13",
        "votação": [],
        "percentagem_votos": []
    },
    {
        "nome": "Edlania Souza",
        "partido": "PV",
        "cargo": "prefeita(o)",
        "vice": "Eduardo Jorge",
        "numero": "43",
        "votação": [],
        "percentagem_votos": []
    },
    {
        "nome": "Paulo Salvatore",
        "partido": "PSOL",
        "cargo": "prefeita(o)",
        "vice": "Luciana Genro",
        "numero": "50",
        "votação": [],
        "percentagem_votos": []
    },
    {
        "nome": "Victória Gandolfi",
        "partido": "REDE",
        "cargo": "prefeita(o)",
        "vice": "Marina Silva",
        "numero": "18",
        "votação": [],
        "percentagem_votos": []
    }

]

# contabilizando votos válidos, brancos e nulos
# pode digitar branco

votos_brancos = []
votos_nulos = []
votos_validos = []
percentagem_votos = []


def exibir_contagem():
    total_votos = 0
    print()
    print("Votos válidos de cada candidato: ")
    print()
    for candidato in candidatos:
        print("{}: {} votos válidos".format(candidato["nome"], len(candidato["votação"])))
        # print(candidato["nome"] + ": " + str(len(candidato["votação"])))
        total_votos += len(candidato["votação"])
    return total_votos


def exibir_resultado(total_votos):
    for candidato in candidatos:
        percentagem = len(candidato["votação"])/total_votos
        print("{}: {}% do total de votos válidos da eleição.".format(candidato["nome"], percentagem))
        percentagem_votos.append(percentagem)
        for percentagens in percentagem_votos:
            if percentagens > total_votos / 2:
                print("O vencedor da eleição é {} ({}) com um total de {} votos válidos.".format(candidato["nome"], candidato["partido"], candidato[""]))
            else:
                pass


def exibir_total():
    print("Contagem de votos: ")
    print()
    print("Votos válidos: {}\nVotos brancos: {}\nVotos nulos: {}".format(len(votos_validos), len(votos_brancos), len(votos_nulos)))
    print()

# print("Camila Campos: {} votos válidos\nMonica Rezende: {} votos válidos\nEdlania Souza: {} votos válidos\nPaulo Salvatore: {} votos válidos\nVictoria Gandolfi: {} votos válidos\n".format(len(candidatos[0]["votação"])))


def encerrar_votacao():
    print("Votação encerrada.")
    print()
    exibir_total()
    exibir_contagem()
    exibir_resultado()


def pegar_voto(voto):
    if voto == "branco":
        votos_brancos.append(voto)
        print("Voto computado! Obrigada por fazer seu papel de cidadão.\nO país agradece!")
    elif voto == "encerrar votação":
        encerrar_votacao()
    else:
        for candidato in candidatos:
            if voto == candidato["numero"] and candidato["cargo"] == "prefeita(o)":
                proximo_passo = input("Seu voto será computado para o(a) candidato {}. Digite 'confirma' para confirmar, 'corrige' para corrigir e 'cancela' para cancelar a aplicação.".format(candidato["nome"]))
                if proximo_passo == "confirma":
                    votos_validos.append(voto)
                    print("Voto computado! Obrigada por fazer seu papel de cidadão.\nO país agradece!")
                    candidato["votação"].append(voto)
                    return candidato
                elif proximo_passo == "corrige":
                    voto = input("Informe seu voto para a Prefeitura de São Paulo (dois dígitos ou 'branco', caso deseje votar em branco): ")
                    return pegar_voto(voto)
                elif proximo_passo == "cancela":
                    print("Seu voto foi cancelado. Inicie novamente.")
                    voto = input("Informe seu voto para a Prefeitura de São Paulo (dois dígitos ou 'branco', caso deseje votar em branco): ")
                    return pegar_voto(voto)
        else:
            confirmacao = input("Candidato não selecionado. Voto será contabilizado como nulo. Para confirmar aperte enter.")
            if confirmacao == "":
                votos_nulos.append(voto)
                print("Voto computado! Obrigada por fazer seu papel de cidadão.\nO país agradece!")
            else:
                voto = input("Informe seu voto para a Prefeitura de São Paulo (dois dígitos ou 'branco', caso deseje votar em branco): ")
                return pegar_voto(voto)


voto = input("Informe seu voto para a Prefeitura de São Paulo (dois dígitos ou 'branco', caso deseje votar em branco): ")

pegar_voto(voto)

"""
7 - Coloque um comando 'encerrar votação' que finaliza a votação e exibe as informações abaixo:
- Informar a quantidade de votos válidos, brancos e nulos;
- Checar se o político mais votado possui mais de 50% dos votos ou se haverá segundo turno.
- Caso tenha vencedor: Informar quem ganhou e qual a porcentagem de votos que ele teve;
- Exibir na tela um político por linha, com a quantidade de votos recebidos e a porcentagem equivalente.
"""
