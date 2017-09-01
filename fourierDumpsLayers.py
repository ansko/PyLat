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
    folder = '/home/anton/Article_MD/Computations/1st conf/mixed ok/300K/relaxation+wiggle/7th wiggle cycle (1455489)/Dumps/'
    allStresses = []
    for i in range(int(25000 / step) + 1):
        fname = folder + 'ALLstress.' + str(i * step * 100)
        sp = StressParser(fname)
        allStresses.append(sp.stresses())
    lx = sp.lx()
    ly = sp.ly()
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
                    
    for k in range(15):
        if len(l1) / 2**k < 4:
            continue
        print('------------------', k, '-----------------')
        for arrNum, arr in enumerate([l1, l2, l3, l4, l5, l6, l7]):
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
    
            
        
#    for k in range(15):
#        if (l / 2**k < 4):
#            continue
#        print('------------------', k, '-----------------')
#        for i in range(int(10 * multiplier), len(allStresses[0])):
#            s = []
#            for stresses in allStresses:
#                s.append(stresses[i] / lx / ly / 1 * multiplier)
#                for ii in range(k):
#                    period = len(s)
#                    for j in range(period - 1):
#                        s[j] += s[j + 1]
#                        s[j] /= 2
#                    if len(s) % 2 == 0:
#                        s = s[::2]
#                    else:
#                        endelement = s[-1]
#                        s = s[::2]
#                        s.append(endelement)
#            (a0, a1, b1) = approximate(s)
#            err = error(s, a0, a1, b1)
#            magnitude = 5 * math.sqrt(a1**2 + b1**2)
#            print(i / multiplier, magnitude, err)


main()
