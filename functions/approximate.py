import math


def approximate(pressures, periodsNum=1):
    i = a0 = a1 = a2 = b1 = b2 = 0
    suma0 = suma1 = suma2 = sumb1 = sumb2 = magnitude = 0

    period = int(len(pressures) / periodsNum)

    for i in range(len(pressures)):
        suma0 += float(pressures[i])
        suma1 += float(pressures[i]) * math.cos(2 * math.pi / period * (i + 1))
        sumb1 += float(pressures[i]) * math.sin(2 * math.pi / period * (i + 1))
        suma2 += float(pressures[i]) * math.cos(4 * math.pi / period * (i + 1))
        sumb2 += float(pressures[i]) * math.sin(4 * math.pi / period * (i + 1))

    a0 = suma0 / period / periodsNum
    a1 = 2 * suma1 / period / periodsNum
    a2 = 2 * suma2 / period / periodsNum
    b1 = 2 * sumb1 / period / periodsNum
    b2 = 2 * sumb2 / period / periodsNum

    return (a0, a1, b1)
