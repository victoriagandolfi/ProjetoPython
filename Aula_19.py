# if/else em uma linha
"""
Biblioteca time

"""

import time

cronometro = 0


while True:
    """    cronometro += 1

    print("Segundos:{}".format(cronometro))

    time.sleep(1)"""

    inicio = time.clock()
    final = 0


    cronometro += 1

    horas = (cronometro - cronometro % (60 * 60)) / (60 * 60)
    minutos = (cronometro - cronometro % 60) / 60 - (horas * 60)
    segundos = cronometro % 60

    if cronometro == 3560:
        break


    time.sleep(1)

print("Hora: {:.0f} - Minutos: {:.0f} - Segundos : {:.0f}".format(horas, minutos, segundos))

final = time.clock() - inicio
print("A aplicação demorou {} segundos para finalizar.".format(final))

# time.time - em segundos o tempo do PC
# time.clock - em segundos o tempo desde que a aplicação iniciou
