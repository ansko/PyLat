import math


def approximate(pressures):
    i = a0 = a1 = a2 = b1 = b2 = 0
    suma0 = suma1 = suma2 = sumb1 = sumb2 = magnitude = 0

    period = len(pressures)

    for i in range(period):
        suma0 += float(pressures[i])
        suma1 += float(pressures[i]) * math.cos(2 * math.pi / period * (i + 1))
        sumb1 += float(pressures[i]) * math.sin(2 * math.pi / period * (i + 1))
        suma2 += float(pressures[i]) * math.cos(4 * math.pi / period * (i + 1))
        sumb2 += float(pressures[i]) * math.sin(4 * math.pi / period * (i + 1))

    a0 = suma0 / period
    a1 = 2 * suma1 / period
    a2 = 2 * suma2 / period
    b1 = 2 * sumb1 / period
    b2 = 2 * sumb2 / period
    magnitude = 5 * math.sqrt(a1**2 + b1**2)

    return (a0, a1, b1)
