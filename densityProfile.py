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
                   s + '4th wiggle cycle (1427696)/',
                   s + '5th wiggle cycle ok (1436418)/',
                   s + '6th wiggle cycle (1432418)/',
                   s + '7th wiggle cycle (1455489)/']
    elif systemName == 'segregated':
        s = '1st conf/segregated/300K/'
        folders = [s + '1st wiggle cycle (1414047)/',
                   s + '2nd wiggle cycle (1426324)/',
                   s + '3rd wiggle cycle ok (1427860)/',
                   s + '4th wiggle cycle after corrupted (1427697)/',
                   s + '5th wiggle cycle (1428078)/',
                   s + '6th wiggle cycle (1432422)/',
                   s + '7th cycle wiggle (1440140)/']
    elif systemName == 'PA6x20':
        s = 'PA6x20/'
        folders = [s + '2024799/']
    elif systemName == '5x20':
        s = '/BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/'
        folders = [s + '1795407 - wiggle no dumps/',
                   s + '1797475 - wiggle 1/',
                   s + '1799268 - wiggle2/',
                   s + '1808725 - wiggle3/']
    elif systemName == '10x20':
        s = '/BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/'
        folders = [s + '1795426 - wiggle no dumps/',
                   s + '1797474 - wiggle 1/',
                   s + '1799293 - wiggle2/',
                   s + '1808726 - wiggle3/']
    else:
        folders = None
    dp = DataParser(mainFolder + folders[0] + 'co.50000.data')
    zlo = dp.zlo()
    zhi = dp.zhi()
    lx = dp.xhi() - dp.xlo()
    ly = dp.yhi() - dp.ylo()
    lz = dp.zhi() - dp.zlo()
    masses = dp.masses()
    profile = [[0, 0, 0, 0] for i in range(int((zhi - zlo + 1 + lz) * multiplier + 1))]
    for folder in folders:
        for i in range(1, 51):
            fname = mainFolder + folder + 'co.' + str(5 * i) + '0000.data'
            dp = DataParser(fname)
            dp.parseAtoms()
            atoms = dp.atoms()
            for atomNum, atom in enumerate(atoms):
                if atomNum == 0:
                    continue
                if systemName == '10x20':
                    if atom[5] < 15.5:
                        z = int(multiplier * (atom[5] + lz - zlo - 21.5))
                    else:
                        z = int(multiplier * (atom[5] - zlo - 21.5))
                else:
                    z = int(multiplier * (atom[5] - zlo))
                    #z = 1000 + int(multiplier * atom[5])
                z -= 9
                mass = masses[atom[1]]
                profile[z][0] += mass
                profile[z][definePhase(systemName, atomNum)] += mass
    for z, value in enumerate(profile):
        if value[0] / lx / ly * multiplier / len(folders) / 50 / 0.602 != 0:
            print(z / multiplier,
                  value[0] / lx / ly * multiplier / len(folders) / 50 / 0.602,
                  value[1] / lx / ly * multiplier / len(folders) / 50 / 0.602,
                  value[2] / lx / ly * multiplier / len(folders) / 50 / 0.602,
                  value[3] / lx / ly * multiplier / len(folders) / 50 / 0.602)
                  
                  
densityProfile()
