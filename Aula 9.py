"""def somar(*numeros):
    return sum(numeros)


resultado = somar(13, 45, 7, 9)

print(resultado)"""

"""LISTA

count (quantas ocorrências com tal número)
lista.count(numero)
set (números diferentes na lista)
set(lista)
index (índice do elemento)
lista.index(numero)
(se tiver ami de uma vez mesmo número, aparece primeira posição que tem o número. meiocomo procv)

FUNÇÕES
split e joint
while (for sem saber quantas vezes rodar)

while True:
    nome = input()
    
    if nome == "sair":
        break
    
    print(nome)
    
    OU
    
nome = ""
while nome != "sair":
    nome = input(Nome:)
    print(nome)
    
SPLIT E REVERSE
nome = "Paulo Salvatore"
nome_separado = nome.split(" ")
print(nome_separado)
nome_reerso = nome.reverse()"""

"""Aula 5 - início
    Dicionário:
    dicionáreio funciona como lista em que é possível nomear os índices
    {} ao invés de []"""


"""pessoas = {
    "SP": 447,
    "MG": 586,
    "RJ": 1023
}

print(pessoas)
print(pessoas["SP"])
print(pessoas.get("SS"))"""
"""

refeicoes = {
    "ITALIA": 20,
    "JAPA": 80,
    "TAI": 50,
    "BRASUCA": 40,
    "FRANCESA": 100
}

refeicoes["CHINA"] = 15


print(refeicoes)


for refeicao in refeicoes:
    preco = refeicoes[refeicao]
    print(refeicao)
    print(preco)
    print()
    
for indice in refeicoes:
    print(indice)
    valor = refeicoes[indice]
    print(valor)

for indice in range(len(refeicao)):
    print(indice)
    refeicao1 = refeicao[indice]
    print(refeicao1)

print(refeicoes.get("Coxinha"))


def pegarrefeicao(indice):
    refeicao = refeicoes.get(indice)

    if refeicao == None:
        print("Refeição não existe")
    else:
        print("Refeição: {}".format(refeicao))
    return refeicao


custo1 = pegarrefeicao("Salada de Frutas")
custo2 = pegarrefeicao("Panettone")
conta = 0
conta = conta + custo1
conta = conta + custo2
print(conta)

del refeicoes["Salada de Frutas"]

print(refeicoes)

"""

precos = {
    "banana": 4,
    "maçã": 2,
    "laranja": 1.5,
    "pera": 3
}

estoques = {
    "banana": 6,
    "maçã": 0,
    "laranja": 32,
    "pera": 15
}
"""
for fruta in precos:
    preco = precos[fruta]
    estoque = estoques[fruta]
    print("Fruta {}".format(fruta))
    print("\tPreço {}".format(preco))
    print("\tEstoque {}".format(estoque))

# CASAS DECIMAIS: :.2f

total = 0

for fruta in estoques:
    preco = precos[fruta]
    estoque = estoques[fruta]
    total += preco * estoque
    print("O valor total do estoque é R$ {:.2f}".format(total))
"""
"""
mantimentos = ["banana", "laranja", "maçã"]


def computar_compra(mantimento):
    total = 0

    for fruta in mantimento:
        preco = precos[fruta]
        total += preco
        print("O valor total da compra é R$ {:.2f}.".format(total))
    return total


computar_compra(mantimentos)
"""

""" Exercicio mantimentos versão 1
mantimentos = ["banana", "laranja", "maçã"]


def computar_compra(mantimento):
    total = 0

    for fruta in mantimento:
        preco = precos[fruta]
        estoque = estoques[fruta]
        if estoque > 0:
            total += preco
            estoques[fruta] -= 1
            print("Parabéns! A compra foi realizada com sucesso.")
            print("A fruta {} foi comprada.".format(fruta))
            print("O preço pago pela fruta {} foi de R$ {:.2f}.".format(fruta, preco))
            print("Após sua compra, o volume de estoque da fruta {} é de {}.".format(fruta, estoque))
        else:
            print("O produto selecionado escontra-se indisponível no estoque.")
    return total


total_compra = computar_compra(mantimentos)
print("O valor total da compra é R$ {:.2f}.".format(total_compra))"""

""" Exercicio mantimentos versão 2
mantimentos = ["banana", "laranja", "maçã"]


def computar_compra(mantimento):
    total = 0

    for fruta in mantimento:
        preco = precos[fruta]
        estoque = estoques[fruta]
        if estoque > 0:
            total += preco
            estoques[fruta] -= 1
            print("Parabéns! A compra foi realizada com sucesso.")
            print("\tA fruta {} foi comprada.".format(fruta))
            print("\tO preço pago pela fruta {} foi de R$ {:.2f}.".format(fruta, preco))
            print("\tApós sua compra, o volume de estoque da fruta {} é de {}.".format(fruta, estoque))
        else:
            print("O produto selecionado escontra-se indisponível no estoque.")
    print("\tO valor total da compra é R$ {:.2f}.".format(total))
    return total


total_compra = computar_compra(mantimentos)"""

"""Exercicio mantimentos avançado:

def computar_compra(mantimento):
    total = 0

    for fruta in mantimento:
        preco = precos[fruta]
        estoque = estoques[fruta]
        if estoque > 0:
            total += preco
            estoques[fruta] -= 1
            print("Parabéns! A compra foi realizada com sucesso.")
            print("\tA fruta {} foi comprada.".format(fruta))
            print("\tO preço pago pela fruta {} foi de R$ {:.2f}.".format(fruta, preco))
            print("\tApós sua compra, o volume de estoque da fruta {} é de {}.".format(fruta, estoque))
        else:
            print("O produto selecionado escontra-se indisponível no estoque.")
    print("\tO valor total da compra é R$ {:.2f}.".format(total))
    return total


mantimentos = []

frutas_disponiveis = list(precos.keys())
print("As frutas disponíveis são {}.".format("; ".join(frutas_disponiveis))) # "\n- "


while True:
    comprar_fruta = input("Qual fruta você deseja comprar? ")

    if comprar_fruta == "comprar":
        computar_compra(mantimentos)
        break
    else:
        mantimentos.append(comprar_fruta)"""







