import requests
import json

id_politico = 1

url = "http://politicos.olhoneles.org/api/v0/politicians/{}".format(id_politico)
conteudo_url = requests.get(url)
conteudo_json = json.loads(conteudo_url.text)

"""
def varrer_lista_dicionarios(lista, chave, exibicao):
    print(exibicao + ": ")
    for item in lista:
        print("\t" + item[chave])


def formatar_booleano(variavel):
    if variavel:
        return "Sim"
    else:
        return "Não"


def pegar_valor_dicionario(caminho, base):
    try:
        for item in caminho:
            base = base[item]
    except:
        base = "Valor não encontrado."
    return base
"""
"""
nomes_alternativos = conteudo_json["alternative_names"]
varrer_lista_dicionarios(nomes_alternativos, "name", "Nomes Alternativos")


candidaturas = conteudo_json["candidacies"]
"""
"""
for indice, candidatura in enumerate(candidaturas):
    print("{}ª Candidatura: ".format(indice + 1))
    status = candidatura["candidacy_status"]["name"]
    print("/tStatus:" + status)
    eleito = formatar_booleano(candidatura["elected"])
    print("\tEleito:" + eleito)

lista_caminho = ["candidacy_status", "name"]
for indice, candidatura in enumerate(candidaturas):
    valor = pegar_valor_dicionario(lista_caminho, candidatura)
    print(valor)


for indice, candidatura in enumerate(candidaturas):
    valor = pegar_valor_dicionario(["political_office", "name"], candidatura)
    print(valor)

for indice, candidatura in enumerate(candidaturas):
    valor = pegar_valor_dicionario(["city", "name"], candidatura)
    print(valor)

for indice, candidatura in enumerate(candidaturas):
    status = candidatura["candidacy_status"]["name"]
    print("/tStatus:" + status)
    eleito = formatar_booleano(candidatura["elected"])
    print("\tEleito:" + eleito)

for indice, candidatura in enumerate(candidaturas):
    valor = pegar_valor_dicionario(["state", "name"], candidatura)
    print(valor)
"""
"""
Nomes alternativos
alternative_names   name

Candidaturas
candidacies
    Nome do Status candidacy_status    name
    Cidade  city    name
    Eleito  elected
    Cargo political_office  name
    Estado  state   name
    
CPF cpf
Etnia   ethnicity   name"""

# dicionario.keys

def varrer_lista_dicionarios(lista, chave, exibicao):
    print(exibicao + ": ")
    for item in lista:
        print("\t" + item[chave])


def formatar_booleano(variavel):
    if variavel:
        return "Sim"
    else:
        return "Não"


def pegar_valor_dicionario(caminho, base):
    try:
        for item in caminho:
            base = base[item]
    except:
        base = "Valor não encontrado."
    return base


nome_cartorio = conteudo_json["name"]
print("Nome civil: " + nome_cartorio)

nomes_alternativos = conteudo_json["alternative_names"]
varrer_lista_dicionarios(nomes_alternativos, "name", "Nomes Alternativos")

cpf = conteudo_json["cpf"]
print("CPF: {}.{}.{}-{}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9]))

data_nascimento = conteudo_json["date_of_birth"]
data_nascimento = data_nascimento.split("-")
data_nascimento.reverse()
data_nascimento = "/".join(data_nascimento)
print("Data de nascimento: " + data_nascimento)

genero = conteudo_json["gender"]
if genero == "M":
    print("Gênero: masculino")
elif genero == "F":
    print("Gênero: feminino")

etnia = pegar_valor_dicionario(["ethnicity", "name"], conteudo_json)
print("Etnia: " + etnia)

estado_civil = pegar_valor_dicionario(["marital_status", "name"], conteudo_json)
estado_civil = estado_civil[:(len(estado_civil) - 4)]
if genero == "F":
    print("Estado civil: " + estado_civil + "a")
elif genero == "M":
    print("Estado civil: " + estado_civil + "o")

nacionalidade = pegar_valor_dicionario(["nationality", "name"], conteudo_json)
print("Nacionalidade: " + nacionalidade)

estado_atual = pegar_valor_dicionario(["state", "name"], conteudo_json)
print("Estado atual: " + estado_atual)

educacao = conteudo_json["education"]
escolarizacao = pegar_valor_dicionario(["name"], educacao)
print("Nível de escolarização: " + escolarizacao)

ocupacao = pegar_valor_dicionario(["occupation", "name"], conteudo_json)
print("Profissão: " + ocupacao)


partidos = conteudo_json["political_parties"]

for indice, partido in enumerate(partidos):
    print("{}º partido: ".format(indice + 1))
    data_inicial = pegar_valor_dicionario(["date_start"], partido)
    print("\tData inicial: " + data_inicial)
    data_final = pegar_valor_dicionario(["date_end"], partido)
    if data_final:
        print("\tData final: " + str(data_final))
    if not data_final:
        print("\tData final: Valor inexistente.")
    nome_partido = pegar_valor_dicionario(["political_party", "name"], partido)
    print("\tNome do partido:" + nome_partido)
    sigla_partido = pegar_valor_dicionario(["political_party", "siglum"], partido)
    print("\tSigla do partido: " + sigla_partido)
    tse = pegar_valor_dicionario(["political_party", "tse_number"], partido)
    print("\tNúmero do TSE: " + str(tse))

candidaturas = conteudo_json["candidacies"]

for indice, candidatura in enumerate(candidaturas):
    print("{}ª Candidatura: ".format(indice + 1))
    cargo = pegar_valor_dicionario(["political_office", "name"], candidatura)
    print("\tCargo:" + cargo)
    status = candidatura["candidacy_status"]["name"]
    print("\tStatus:" + status)
    cidade = pegar_valor_dicionario(["city", "name"], candidatura)
    print("\tCidade:" + cidade)
    estado = candidatura["state"]["name"]
    print("\tEstado:" + estado)
    eleito = formatar_booleano(candidatura["elected"])
    print("\tEleito:" + eleito)



