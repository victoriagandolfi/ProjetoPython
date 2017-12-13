"""from math import sqrt


sqrt(5)

# OU

import math

math.sqrt(50)

help("math")

import math as matematica

print(matematica.sqrt(50))

"""
""" ARGS

def numero(*args):
    print(args)


numero(1, 2, 3, 4)"""

# MAX e MIN

"""def nome_funcao(*args):
    print("Args recebido: {}".format(args))
    maior_numero = max(args)
    print("Maior número: {}".format(maior_numero))
    menor_numero = min(args)
    print("Menor número: {}".format(menor_numero))


nome_funcao(1, 6, 2, 5, 78, 98)"""

# ABS
"""
numero = -60
print(abs(numero))"""

# TYPE (tipo da variável)

"""print(type("Victoria"))
print(type(22))
print(type(22.6))

nome = "Victoria"
print(type(nome))

idade = int(input("idade:"))
print(type(idade))"""

"""numero = float(input())
if (type(numero) == float):
    print("O número é um float")"""

"""import math

def custo_hotel(noites):
    custo_total = noites * 140
    return custo_total

noites = int(input("Quantas noites passará no hotel? "))
print(int(custo_hotel(noites)))


def custo_aviao(n):
    if n == "São Paulo":
        return 312
    elif n == "Porto Alegre":
        return 447
    elif n == "Recife":
        return 831
    elif n == "Manaus":
        return 986


n = input("Para qual cidade deseja ir? ")
print(int(custo_aviao(n)))

def custo_carro(dias):
    custo_total = dias * 40
    if dias >= 7:
        return custo_total - 50
    elif 3 <= dias < 7:
        return custo_total - 20
    else:
        return custo_total


dias = int(input("Por quantos dias alugará o carro?"))
print(int(custo_carro(dias)))


def gastos_extras(extra):
    return extra


extra = int(input("Calcula que haverá gasto extra de quanto? "))
print(gastos_extras(extra))


def soma(*args):
    return sum(args)


def viagem():
    return soma(custo_carro(dias), custo_aviao(n), custo_hotel(noites), gastos_extras(extra))


viagem()
print("O custo total da viagem esperada será de R$ {:.2f}.".format(viagem()))"""










