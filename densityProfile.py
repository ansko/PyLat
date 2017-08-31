#!/usr/bin/env python3
# coding utf-8

import pprint
pprint=pprint.PrettyPrinter(indent=1).pprint

from Classes.DataParser import DataParser
from Classes.Options import Options

from functions.definePhase import definePhase


def densityProfile():
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
    elif systemName == 'segregated':
        s = '1st conf/segregated/300K/'
        folders = [s + '1st wiggle cycle (1414047)/',
                   s + '2nd wiggle cycle (1426324)/',
                   s + '3rd wiggle cycle ok (1427860)/',
                   s + '4th wiggle cycle after corrupted (1427697)/']
    elif systemName == 'PA6x20':
        s = 'PA6x20/'
        folders = [s + '2024799/']
    else:
        folders = None
    dp = DataParser(mainFolder + folders[0] + 'co.50000.data')
    zlo = dp.zlo()
    zhi = dp.zhi()
    lx = dp.xhi() - dp.xlo()
    ly = dp.yhi() - dp.ylo()
    masses = dp.masses()
    profile = [[0, 0, 0, 0] for i in range(int((zhi - zlo + 1) * multiplier))]
    for folder in folders:
        for i in range(1, 51):
            fname = mainFolder + folder + 'co.' + str(5 * i) + '0000.data'
            dp = DataParser(fname)
            dp.parseAtoms()
            atoms = dp.atoms()
            for atomNum, atom in enumerate(atoms):
                if atomNum == 0:
                    continue
                z = int(multiplier * (atom[5] - zlo))
                mass = masses[atom[1]]
                profile[z][0] += mass
                profile[z][definePhase(systemName, atomNum)] += mass
    for z, value in enumerate(profile):
        print(z / multiplier,
              value[0] / lx / ly * multiplier / len(folders) / 50 / 0.602,
              value[1] / lx / ly * multiplier / len(folders) / 50 / 0.602,
              value[2] / lx / ly * multiplier / len(folders) / 50 / 0.602,
              value[3] / lx / ly * multiplier / len(folders) / 50 / 0.602)
densityProfile()