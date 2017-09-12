import math


def approximate(pressures, harmonicNum=1):
    i = a0 = a1 = a2 = b1 = b2 = 0
    suma0 = sumaN = sumbN = 0

    period = int(len(pressures))

    for i in range(len(pressures)):
        suma0 += float(pressures[i])
        sumaN += float(pressures[i]) * math.cos(2 * harmonicNum * math.pi / period * (i + 1))
        sumbN += float(pressures[i]) * math.sin(2 * harmonicNum * math.pi / period * (i + 1))

    a0 = suma0 / period
    aN = 2 * sumaN / period
    bN = 2 * sumbN / period

    return (a0, aN, bN)
