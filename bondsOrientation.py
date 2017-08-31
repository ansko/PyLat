#!/usr/bin/env python3
# coding utf-8

import pprint
pprint=pprint.PrettyPrinter(indent=1).pprint

from Classes.DataParser import DataParser
from Classes.Options import Options

from functions.definePhase import definePhase
from functions.utils import orderParameter


def bondsOrientation():
    o = Options()
    systemName = o.getProperty('systemName')
    multiplier = o.getProperty('multiplier')
    mainFolder = o.getProperty('mainFolder')
    if systemName == 'mixed':
        s = '1st conf/mixed ok/300K/relaxation+wiggle/'
        folders = [s + '1st wiggle cycle (1414048 )/',
                   s + '2nd wiggle cycle (1426323)/',
                   s + '3rd wiggle cycle(1427113)/',
                   s + '4th wiggle cycle (1427696)/']
        bondTypesToSkip = [1, 2, 6, 7, 9, 10, 13, 15]
    elif systemName == 'segregated':
        s = '1st conf/segregated/300K/'
        folders = [s + '1st wiggle cycle (1414047)/',
                   s + '2nd wiggle cycle (1426324)/',
                   s + '3rd wiggle cycle ok (1427860)/',
                   s + '4th wiggle cycle after corrupted (1427697)/']
        bondTypesToSkip = [1, 2, 6, 7, 9, 10, 13, 15]
    elif systemName == 'PA6x20':
        s = 'PA6x20/'
        folders = [s + '2024799/']
        bondTypesToSkip = [1, 3, 6, 8, 11]
    else:
        folders = None
        bondTypesToSkip = None
    dp = DataParser(mainFolder + folders[0] + 'co.50000.data')
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
            atoms = dp.atoms()
            bonds = dp.bonds()
            for bondNum, bond in enumerate(bonds):
                if bondNum == 0:
                    continue
                if bond[0] in bondTypesToSkip:
                    continue
                dx = abs(atoms[bond[1]][3] - atoms[bond[2]][3])
                dx = min(dx, abs(lx - dx))
                dy = abs(atoms[bond[1]][4] - atoms[bond[2]][4])
                dy = min(dx, abs(ly - dy))
                dz = abs(atoms[bond[1]][5] - atoms[bond[2]][5])
                dz = min(dz, abs(lz - dz))
                length = (dx**2 + dy**2 + dz**2)**0.5
                cosTheta = dz / length
                parameter = orderParameter(cosTheta)
                z = int(multiplier * (atoms[bond[2]][5] - zlo))
                profile[z][0] += 1
                profile[z][1] += parameter
    for z, value in enumerate(profile):
        if value[0] == 0:
            continue
        print(z / multiplier,
              value[1] / value[0])

bondsOrientation()
