#!/usr/bin/env python3
# coding utf-8

import math
import numpy as np
import pprint
pprint=pprint.PrettyPrinter(indent=1).pprint

from Classes.Options import Options
from Classes.StressParser import StressParser

from functions.approximate import approximate
from functions.definePhase import definePhase
from functions.error import error
from functions.utils import clayRanges


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
    zlo = sp.zlo()
    soft = [0 for i in range(len(allStresses))]
    hard = [0 for i in range(len(allStresses))]
    [bot, top] = clayRanges(systemName)
    print(top - bot)
    clayThickness = 9.2
    for i, stresses in enumerate(allStresses):
        for z, stress in enumerate(stresses):
            if bot < zlo + z < top:
                hard[i] += stress / lx / ly / clayThickness
            else:
                soft[i] += stress / lx / ly / (lz - clayThickness)
    for k in range(1, 10):
        if len(soft) / 2**k < 4:
            continue
        print('------------------', k, '-----------------')
        if systemName in ['mixed', 'segregated', '5x20', '10x20']:
            layers = [soft, hard]
        else:
            layers = [soft, ]
        for arrNum, arr in enumerate(layers):
            for i in range(k):
                arr1 = np.array(arr)
                arr1 += arr
                arr1 = arr1 / 2
                arr1 = arr1[::2]
                arr = list(arr1)
                harmonicNum=len(folders)
                (a0, aN, bN) = approximate(arr, harmonicNum=harmonicNum)
                err = error(arr, a0, aN, bN, harmonicNum=harmonicNum)
                period = int(len(arr))
                magnitude = 5 * math.sqrt(aN**2 + bN**2)
                print(arrNum, i, magnitude, err)
                
            
main()
