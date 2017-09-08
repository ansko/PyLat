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
        folders = [(mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' + 
                    '1st wiggle cycle (1414048 )/Dumps/'),
                   (mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' +
                    '2nd wiggle cycle (1426323)/Dumps/'),
                   (mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' +
                    '3rd wiggle cycle(1427113)/Dumps/'),
                   (mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' +
                    '4th wiggle cycle (1427696)/Dumps/'),
                   (mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' +
                    '5th wiggle cycle ok (1436418)/Dumps/'),
                   (mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' +
                    '6th wiggle cycle (1432418)/Dumps/'),
                   (mainFolder + '1st conf/mixed ok/300K/relaxation+wiggle/' +
                    '7th wiggle cycle (1455489)/Dumps/')]
    elif systemName == 'segregated':
        folders = [(mainFolder + '1st conf/segregated/300K/' +
                    '1st wiggle cycle (1414047)/Dumps/'), 
                   (mainFolder + '1st conf/segregated/300K/' +
                    '2nd wiggle cycle (1426324)/Dumps/'),
                   (mainFolder + '1st conf/segregated/300K/' +
                    '3rd wiggle cycle ok (1427860)/Dumps/'),
                   (mainFolder + '1st conf/segregated/300K/' +
                    '4th wiggle cycle after corrupted (1427697)/Dumps/'),
                   (mainFolder + '1st conf/segregated/300K/' +
                    '5th wiggle cycle (1428078)/Dumps/'),
                   (mainFolder + '1st conf/segregated/300K/' +
                    '6th wiggle cycle (1432422)/Dumps/'),
                   (mainFolder + '1st conf/segregated/300K/' +
                    '7th cycle wiggle (1440140)/Dumps/')]
    elif systemName == '5x20':
        folders = [(mainFolder + 'BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/' +
                    '1797475 - wiggle 1/Dumps/'),
                   (mainFolder + 'BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/' +
                    '1799268 - wiggle2/Dumps/')]
        # corrupted
        #folder = (mainFolder +
        #          'BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/1808725 - wiggle3/Dumps/')
    elif systemName == '10x20':
        folders = [(mainFolder + 'BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/' +
                    '1797474 - wiggle 1/Dumps/'),
                   (mainFolder + 'BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/' +
                    '1799293 - wiggle2/Dumps/'),
                   (mainFolder + 'BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/' +
                    '1808726 - wiggle3/Dumps/')]
    elif systemName == 'PA6x20':
        folders = [(mainFolder +
                    'PA6x20/2024799/Dumps/'),]
    
    allStresses = []
    for folder in folders:
        for i in range(int(25000 / step) + 1):
            fname = folder + 'ALLstress.' + str(i * step * 100)
            print(fname)
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
                if 32 * multiplier < z < 37 * multiplier:
                    l1[i] += stress / lx / ly / 4.5
                elif 37 * multiplier < z < 41.5 * multiplier:
                    l2[i] += stress / lx / ly / 5
                elif 0 * multiplier < z < 0.5 * multiplier:
                    l2[i] += stress / lx / ly / 5
                elif 0.5 * multiplier < z < 4.5 * multiplier:
                    l3[i] += stress / lx / ly / 4
                elif 4.5 * multiplier < z < 9 * multiplier:
                    l4[i] += stress / lx / ly / 4
                elif 9 * multiplier < z < 13.5 * multiplier:
                    l5[i] += stress / lx / ly / 5
                elif 13.5 * multiplier < z < 18 * multiplier:
                    l6[i] += stress / lx / ly / 4
                elif 18 * multiplier < z < 23 * multiplier:
                    l7[i] += stress / lx / ly / 4
            elif systemName == '10x20':
                if 31 * multiplier < z < 36.5 * multiplier:
                    l1[i] += stress / lx / ly / 4
                elif 36.5 * multiplier < z < 41 * multiplier:
                    l2[i] += stress / lx / ly / 4.5
                elif 41 * multiplier < z < 45.5 * multiplier:
                    l3[i] += stress / lx / ly / 4.5
                elif 45.5 * multiplier < z < 64 * multiplier:
                    l4[i] += stress / lx / ly / 26
                elif 0 * multiplier < z < 8 * multiplier:
                    l4[i] += stress / lx / ly / 26
                elif 8 * multiplier < z < 13 * multiplier:
                    l5[i] += stress / lx / ly / 4.5
                elif 13 * multiplier < z < 17.5 * multiplier:
                    l6[i] += stress / lx / ly / 4.5
                elif 17.5 * multiplier < z < 22 * multiplier:
                    l7[i] += stress / lx / ly / 4
            elif systemName == 'PA6x20':
                l1[i] += stress / lx / ly / lz
                    
    for k in range(1, 15):
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
                arr1 = arr1 / 2
                arr1 = arr1[::2]
                arr = list(arr1)
                (a0, a1, b1) = approximate(arr1, periodsNum=len(folders))
                err = error(arr1, a0, a1, b1)
                magnitude = 5 * math.sqrt(a1**2 + b1**2)
                print(arrNum, i, magnitude, err)
                
    
            
main()
