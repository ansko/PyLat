import math


def error(pressures, a0, aN, bN, harmonicNum=1):
    error = 0
    period = len(pressures)
    for i in range(period):
        error += abs((a0 +
                      aN * math.cos(2 * math.pi * harmonicNum / period * (i+1)) +
                      bN * math.sin(2 * math.pi * harmonicNum / period * (i+1))) -
                      pressures[i])**2
    return math.sqrt(error/len(pressures))
