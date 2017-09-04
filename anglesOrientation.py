#!/usr/bin/env python3
# coding utf-8

import pprint
pprint=pprint.PrettyPrinter(indent=1).pprint

from Classes.DataParser import DataParser
from Classes.Options import Options

from functions.definePhase import definePhase
from functions.utils import orderParameter, clayRanges


def anglesOrientation():
    o = Options()
    systemName = o.getProperty('systemName')
    multiplier = o.getProperty('multiplier')
    mainFolder = o.getProperty('mainFolder')
    if systemName == 'mixed':
        s = '1st conf/mixed ok/300K/relaxation+wiggle/'
        folders = [s + '1st wiggle cycle (1414048 )/',
                   s + '2nd wiggle cycle (1426323)/',
                   s + '3rd wiggle cycle(1427113)/',
                   s + '4th wiggle cycle (1427696)/',
                   s + '5th wiggle cycle ok (1436418)/',
                   s + '6th wiggle cycle (1432418)/',
                   s + '7th wiggle cycle (1455489)/']
        angleTypesToSkip = [4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 20, 21,
                            23, 24, 25, 27, 29]
    elif systemName == 'segregated':
        s = '1st conf/segregated/300K/'
        folders = [s + '1st wiggle cycle (1414047)/',
                   s + '2nd wiggle cycle (1426324)/',
                   s + '3rd wiggle cycle ok (1427860)/',
                   s + '4th wiggle cycle after corrupted (1427697)/',
                   s + '5th wiggle cycle (1428078)/',
                   s + '6th wiggle cycle (1432422)/',
                   s + '7th cycle wiggle (1440140)/']
        angleTypesToSkip = [4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 20, 21,
                            23, 24, 25, 27, 29]
    elif systemName == 'PA6x20':
        s = 'PA6x20/'
        folders = [s + '2024799/']
        angleTypesToSkip = [1, 3, 4, 6, 8, 9, 11, 12, 13, 15, 17, 18, 19, 21]
    elif systemName == '5x20':
        s = '/BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/'
        folders = [s + '1795407 - wiggle no dumps/',
                   s + '1797475 - wiggle 1/',
                   s + '1799268 - wiggle2/',
                   s + '1808725 - wiggle3/']
        angleTypesToSkip = [4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 20, 21,
                            23, 24, 25, 27, 29]
    elif systemName == '10x20':
        s = 'BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/'
        folders = [s + '1795426 - wiggle no dumps/',
                   s + '1797474 - wiggle 1/',
                   s + '1799293 - wiggle2/',
                   s + '1808726 - wiggle3/']
        angleTypesToSkip = [4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 20, 21,
                            23, 24, 25, 27, 29]
    else:
        folders = None
        angleTypesToSkip = None
    dp = DataParser(mainFolder + folders[0] + 'co.50000.data')
    [bottom, top] = clayRanges(systemName)
    zlo = dp.zlo()
    zhi = dp.zhi()
    lx = dp.xhi() - dp.xlo()
    ly = dp.yhi() - dp.ylo()
    lz = dp.zhi() - dp.zlo()
    masses = dp.masses()
    profile = [[0, 0] for i in range(int((zhi - zlo + 1) * multiplier))]
    for folder in folders:
        for i in range(1, 51):
            fname = mainFolder + folder + 'co.' + str(5 * i) + '0000.data'
            dp = DataParser(fname)
            dp.parseAtoms()
            dp.parseBonds()
            dp.parseAngles()
            atoms = dp.atoms()
            angles = dp.angles()
            for angleNum, angle in enumerate(angles):
                if angleNum == 0:
                    continue
                if angle[0] in angleTypesToSkip:
                    continue
                dx = abs(atoms[angle[1]][3] - atoms[angle[3]][3])
                dx = min(dx, abs(lx - dx))
                dy = abs(atoms[angle[1]][4] - atoms[angle[3]][4])
                dy = min(dx, abs(ly - dy))
                dz = abs(atoms[angle[1]][5] - atoms[angle[3]][5])
                dz = min(dz, abs(lz - dz))
                length = (dx**2 + dy**2 + dz**2)**0.5
                cosTheta = dz / length
                parameter = orderParameter(cosTheta)
                #z = int(multiplier * (atoms[angle[2]][5] - zlo))
                z = min(abs(atoms[angle[2]][5] - top),
                        abs(lz + bottom - atoms[angle[2]][5]),
                        abs(bottom - atoms[angle[2]][5]),
                        abs(atoms[angle[2]][5] - top + lz)) * multiplier
                z = int(z)
                profile[z][0] += 1
                profile[z][1] += parameter
    for z, value in enumerate(profile):
        if value[0] == 0:
            continue
        print(z / multiplier,
              value[1] / value[0])

anglesOrientation()
