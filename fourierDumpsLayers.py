#!/usr/bin/env python3
# coding utf-8

import math
import numpy as np
import pprint
pprint=pprint.PrettyPrinter(indent=1).pprint

from Classes.Options import Options
from Classes.StressParser import StressParser

from functions.approximate import approximate
from functions.error import error


def main(step=1):
    o = Options()
    systemName = o.getProperty('systemName')
    multiplier = o.getProperty('multiplier')
    mainFolder = o.getProperty('mainFolder')
    if systemName == 'mixed':
        folder =  (mainFolder +
                   '1st conf/mixed ok/300K/relaxation+wiggle/7th wiggle cycle (1455489)/Dumps/')
    elif systemName == 'segregated':
        folder = (mainFolder +
                  '1st conf/segregated/300K/7th cycle wiggle (1440140)/Dumps/')
    elif systemName == '5x20':
        folder = (mainFolder +
                  'BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/1808725 - wiggle3/Dumps/')
    elif systemName == '10x20':
        folder = (mainFolder +
                  'BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/1808726 - wiggle3/Dumps/')
    elif systemName == 'PA6x20':
        folder = (mainFolder +
                  'PA6x20/2024799/Dumps/')
    
    allStresses = []
    for i in range(int(25000 / step) + 1):
        fname = folder + 'ALLstress.' + str(i * step * 100)
        sp = StressParser(fname)
        allStresses.append(sp.stresses())
    lx = sp.lx()
    ly = sp.ly()
    lz = sp.lz()
    l = 0
    l1 = [0 for i in range(len(allStresses))]
    l2 = [0 for i in range(len(allStresses))]
    l3 = [0 for i in range(len(allStresses))]
    l4 = [0 for i in range(len(allStresses))]
    l5 = [0 for i in range(len(allStresses))]
    l6 = [0 for i in range(len(allStresses))]
    l7 = [0 for i in range(len(allStresses))]
    for i, stresses in enumerate(allStresses):
        for z, stress in enumerate(stresses):
            if systemName == 'mixed':
                if 8 * multiplier < z < 13.5 * multiplier:
                    l1[i] += stress / lx / ly / 4.5
                elif 13.5 * multiplier < z < 17.5 * multiplier:
                    l2[i] += stress / lx / ly / 4.
                elif 17.5 * multiplier < z < 22.5 * multiplier:
                    l3[i] += stress / lx / ly / 5.
                elif 22.5 * multiplier < z < 27 * multiplier:
                    l4[i] += stress / lx / ly / 4.5
                elif 27 * multiplier < z < 31.5 * multiplier:
                    l5[i] += stress / lx / ly / 4.5
                elif 31.5 * multiplier < z < 35.5 * multiplier:
                    l6[i] += stress / lx / ly / 4.
                elif 35.5 * multiplier < z < 41 * multiplier:
                    l7[i] += stress / lx / ly / 4.5
            elif systemName == 'segregated':
                if 8 * multiplier < z < 13.5 * multiplier:
                    l1[i] += stress / lx / ly / 4.5
                elif 13.5 * multiplier < z < 17.5 * multiplier:
                    l2[i] += stress / lx / ly / 4.
                elif 17.5 * multiplier < z < 22 * multiplier:
                    l3[i] += stress / lx / ly / 4.5
                elif 22 * multiplier < z < 26.5 * multiplier:
                    l4[i] += stress / lx / ly / 4.5
                elif 26.5 * multiplier < z < 31 * multiplier:
                    l5[i] += stress / lx / ly / 4.5
                elif 31 * multiplier < z < 35.5 * multiplier:
                    l6[i] += stress / lx / ly / 4.5
                elif 35.5 * multiplier < z < 41 * multiplier:
                    l7[i] += stress / lx / ly / 4.5
            elif systemName == '5x20':
                if -36 * multiplier < z < -31.5 * multiplier:
                    l1[i] += stress / lx / ly / 4.5
                elif -31.5 * multiplier < z < -27 * multiplier:
                    l2[i] += stress / lx / ly / 5
                elif -69 * multiplier < z < -67.5 * multiplier:
                    l2[i] += stress / lx / ly / 5
                elif -67.5 * multiplier < z < -63.5 * multiplier:
                    l3[i] += stress / lx / ly / 4
                elif -63.5 * multiplier < z < -59.5 * multiplier:
                    l4[i] += stress / lx / ly / 4
                elif -59.5 * multiplier < z < -54.5 * multiplier:
                    l5[i] += stress / lx / ly / 5
                elif -54.5 * multiplier < z < -50.5 * multiplier:
                    l6[i] += stress / lx / ly / 4
                elif -50.5 * multiplier < z < -45 * multiplier:
                    l7[i] += stress / lx / ly / 4
            elif systemName == '10x20':
                if 24 * multiplier < z < 29 * multiplier:
                    l1[i] += stress / lx / ly / 4
                elif 29 * multiplier < z < 33.5 * multiplier:
                    l2[i] += stress / lx / ly / 4.5
                elif 33.5 * multiplier < z < 38 * multiplier:
                    l3[i] += stress / lx / ly / 4.5
                elif 38 * multiplier < z < 56 * multiplier:
                    l4[i] += stress / lx / ly / 26
                elif -8 * multiplier < z < 1 * multiplier:
                    l4[i] += stress / lx / ly / 26
                elif 1 * multiplier < z < 5.5 * multiplier:
                    l5[i] += stress / lx / ly / 4.5
                elif 5.5 * multiplier < z < 10 * multiplier:
                    l6[i] += stress / lx / ly / 4.5
                elif 10 * multiplier < z < 15 * multiplier:
                    l7[i] += stress / lx / ly / 4
            elif systemName == 'PA6x20':
                l1[i] += stress / lx / ly / lz
                    
    for k in range(15):
        if len(l1) / 2**k < 4:
            continue
        print('------------------', k, '-----------------')
        if systemName in ['mixed', 'segregated', '5x20', '10x20']:
            layers = [l1, l2, l3, l4, l5, l6, l7]
        else:
            layers = [l1, ]
        for arrNum, arr in enumerate(layers):
            for i in range(k):
                arr1 = arr[1::1]
                arr1.append(arr[0])
                arr1 = np.array(arr1)
                arr1 += arr
                arr1 /= 2
                arr1 = arr1[::2]
                arr = list(arr1)
                (a0, a1, b1) = approximate(arr1)
                err = error(arr1, a0, a1, b1)
                magnitude = 5 * math.sqrt(a1**2 + b1**2)
                print(arrNum, i, magnitude, err)
    
            
main()
