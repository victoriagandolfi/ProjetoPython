# Aula 5
# Exercicio dança de salao:  Escrever uma função que funciona como um jogo, onde o usuário deve digitar as suas escolhas e o programa irá indicar o resultado das escolhas.

"""
def jogo():
    print("Você entrou em um salão")
    direcao = input("Deseja ir para a esquerda ou para a direita?").lower()
    if direcao == "esquerda" or direcao == "e":
        print("Você entrou na sala à esquerda, parece que não tem nada por aqui. Acho melhor você voltar correndo!")
    elif direcao == "direita" or direcao == "d":
        print("Excelente escolha! A sala à direita estava te esperando esse tempo todo! Que maravilhoso isso. Pena que não tem nada aqui para você. :(")
    else:
        print("Você não escolheu nenhuma das portas. Tente novamente.")
        return jogo()


jogo()
"""

# Exercicio par ou ímpar

"""numero = int(input("Insira um número: "))


def numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


if numero_par(numero):
    print("O número {} é par.".format(numero))
else:
    print("O número {} é ímpar.".format(numero))"""

# Exercicio 18 - Praticando: Funções Matemáticas
"""

def pegar_maior_valor(*args):
    print("O maior valor é {}.".format(max(args)))


def pegar_menor_valor(*args):
    print("O menor valor é {}.".format(min(args)))


numero10 = int(input("Escreva um número: "))
numero20 = int(input("Escreva um número: "))
numero30 = int(input("Escreva um número: "))

pegar_maior_valor(numero10, numero20, numero30)

pegar_menor_valor(numero10, numero20, numero30)

numero1 = abs(int(input("Escreva um número positivo: ")))
numero2 = abs(int(input("Escreva um número positivo: ")))
numero3 = abs(int(input("Escreva um número positivo: ")))
numero4 = abs(int(input("Escreva um número negativo: ")))
numero5 = abs(int(input("Escreva um número negativo: ")))
numero6 = abs(int(input("Escreva um número negativo: ")))


pegar_maior_valor(numero1, numero2, numero3, numero4, numero5, numero6)

pegar_menor_valor(numero1, numero2, numero3, numero4, numero5, numero6)


def tipo_variavel(numero):
    return type(numero)


def exibir_formatacao(numero):
    if type(numero) == float:
        print("O número digitado diz respeito a R${:.2f}.".format(numero))
    elif type(numero) == int:
        print("O número digitado diz respito a {:05d}".format(numero))
    elif type(numero) == str:
        print("O número digitado diz respeito a {:>10}".format(numero))
    else:
        print("Esse tipo de variável não está mapeado.")


numero_digitado = int(input("Digite um número inteiro: "))
tipo_variavel(numero_digitado)
exibir_formatacao(numero_digitado)

numero_digitado2 = input("Digite um número como texto: ")
tipo_variavel(numero_digitado2)
exibir_formatacao(numero_digitado2)

numero_digitado3 = float(input("Digite um número como decimal: "))
tipo_variavel(numero_digitado3)
exibir_formatacao(numero_digitado3)

"""
# Lista
"""
lista = [3, 5, 6, 7, 8]
# indice = [0, 1, 2, 3, 4]
print(lista)
print(lista[4])
lista[4] = 2
print(lista)

lista_vazia = []
lista_vazia.append(10)
print(lista_vazia)

quantidade_elementos = len(lista_vazia)
print(quantidade_elementos)

# .append() -> adicionar numeros ao final da lista
# len() -> quantidade de elementos na lista tal
# primeiros_elementos = lista[3:5] (indice 3 ao 4)
# string"""
"""nome = "Paulo Salvatore"
print(nome)
print(nome[:5])
print(nome[6:])""""""
"""
# Exercicio catdogfrog

"""lista = "catdogfrog"
cat = lista[:3]
dog = lista[3:6]
frog = lista[7:]
lista_nova = [cat, dog, frog]
print(lista_nova)"""
"""
animais = ["gato", "cachorro", "morcego"]
print(animais.index("morcego"))
# mostra indice do item da lista lista.index
animais.insert(0, "papagaio")
print(animais)

# for (para cada elemento da lista)

for animal in animais:
    print(animal)"""

"""for numero in lista:
    print(numero)"""

"""for numero in lista:
    print(numero * 2)

for numero in lista:
    variavel = numero * 2
    print(variavel)"""

"""for numero in lista:
    variavel = numero * 3
    if variavel % 2 == 0:
        print(variavel)

numeros = []

for numero in range(3):
    print(numero)
    numero_digitado = int(input("Digite um numero:"))
    print(numero_digitado)
    numeros.append(numero_digitado)

print(numeros)
numeros.sort(reverse=True)# ordem decrescente
print(numeros)"""
"""
lista = [5, 6, 3, 2, 1]

lista_vazia = []

for numero in lista:
    novo_numero = numero ** 2
    lista_vazia.append(novo_numero)

lista_vazia.sort()

print(lista_vazia)"""
"""

numeros = [2, 15, 20, 4, 9]"""

# for numero in numeros:
#    print(numero)

"""for numero in numeros:
    if numero > 3:
        print(numero)

for numero in numeros:
    if numero % 2 == 0:
        print(numero)

for numero in numeros:
    print(numero)

total = 0

for numero in numeros:
    total += numero
    print(total)

# ou total += numero (pega o que ta la e soma)

total = sum(numeros)

print(total)

for numero in numeros:
    sum(numeros)

"""
"""
listanova = []

for numeros in range(11):
    numero = int(input("Digite um número: "))
    listanova.append(numero)
    print(listanova)
    print(len(listanova))



print(listanova[0:3])
print(listanova[8:])



nomes = []

for nome in range(3):
    nome_conteudo = input("Digite seu nome:")
    nomes.append(nome_conteudo)
    nomes.sort()

for nome_conteudo in nomes:
    print(nome_conteudo)
"""

""" Exercicio 19- Lista
lista1 = [23, 3, 10, 100, 9000]"""

# for listinha in lista1:
#     print(listinha)

"""for listinha in lista1:
    if listinha > 3:
        print(listinha)"""

"""for listinha in lista1:
    if listinha % 2 == 0:
        print(listinha)"""

"""total = 0

for listinha in lista1:
    total += listinha

print("A soma dos números listados é {}.".format(total))"""

"""lista2 = []

for algoritmos in range(10):
    listinha = int(input("Insira um número: "))
    lista2.append(listinha)
    quantidade = len(lista2)
    print(quantidade)

(ATÉ ITEM 15)"""



