import math


def error(pressures, a0, a1, b1):
    error = 0
    period = len(pressures)
    for i in range(period):
        error += abs((a0 +
                      a1 * math.cos(2 * math.pi / period * (i+1)) +
                      b1 * math.sin(2 * math.pi / period * (i+1))) - pressures[i])**2
    return math.sqrt(error/len(pressures))
