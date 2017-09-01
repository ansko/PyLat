#!/usr/bin/env python3
# coding utf-8

import math

from Classes.Options import Options
from Classes.StressParser import StressParser

from functions.approximate import approximate
from functions.error import error


def main(step=10):
    o = Options()
    multiplier = o.getProperty('multiplier')
    folder = '/home/anton/Article_MD/Computations/1st conf/mixed ok/300K/relaxation+wiggle/7th wiggle cycle (1455489)/Dumps/'
    allStresses = []
    for i in range(int(25000 / step) + 1):
        fname = folder + 'ALLstress.' + str(i * step * 100)
        sp = StressParser(fname)
        allStresses.append(sp.stresses())
    lx = sp.lx()
    ly = sp.ly()
    lz = sp.lz()
    l = 0
    for stresses in allStresses:
        l = max(l, len(stresses))
    for stresses in allStresses:
        while len(stresses) < l:
            stresses.append(0)
    l = len(allStresses)
    for k in range(15):
        if (l / 2**k < 4):
            continue
        print('------------------', k, '-----------------')
        for i in range(int(10 * multiplier), len(allStresses[0])):
            s = []
            for stresses in allStresses:
                s.append(stresses[i] / lx / ly / 1 * multiplier)
                for ii in range(k):
                    period = len(s)
                    for j in range(period - 1):
                        s[j] += s[j + 1]
                        s[j] /= 2
                    if len(s) % 2 == 0:
                        s = s[::2]
                    else:
                        endelement = s[-1]
                        s = s[::2]
                        s.append(endelement)
            (a0, a1, b1) = approximate(s)
            err = error(s, a0, a1, b1)
            magnitude = 5 * math.sqrt(a1**2 + b1**2)
            print(i / multiplier, magnitude, err)


main()
