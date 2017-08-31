#!/usr/bin/env python3
# coding utf-8

from Classes.DataParser import DataParser
from Classes.Options import Options

from functions.definePhase import definePhase
from functions.utils import clayRanges

def segregation():
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
    [bottom, top]= clayRanges(systemName)
    for folder in folders:
        for i in range(1, 51):
            fname = mainFolder + folder + 'co.' + str(i * 50000) + '.data'
            dp = DataParser(fname)
            dp.parseAtoms()
            lz = dp.zhi() - dp.zlo()
            atoms = dp.atoms()
            distance = 0
            atomsNum = 0
            for atomNum, atom in enumerate(atoms):
                if definePhase(systemName, atomNum) != 2:
                    continue
                distance += min(abs(atom[5] - top), abs(lz + bottom - atom[5]))
                atomsNum += 1
            print(distance / atomsNum, atomsNum)
                
                
segregation()