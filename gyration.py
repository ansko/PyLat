#!/usr/bin/env python3

from Classes.DataParser import DataParser
from Classes.Options import Options

from functions.computeRGyr import computeRGyr
from functions.makeMolecule import makeMolecule
from functions.utils import clayRanges

def printMolecule(molecule, molNum):
    f = open('pics/' + str(molNum) + '.xyz', 'w')
    f.write(str(len(molecule)))
    f.write('\n\n')
    for atom in molecule:
        s = 'C ' + str(atom[1]) + ' ' + str(atom[2]) + ' ' +str(atom[3]) + '\n'
        f.write(s)

def gyration():
    o = Options()
    multiplier = o.getProperty('multiplier')
    systemName = o.getProperty('systemName')
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
        polymerChainsNum = 90
        chainPerCell = 10
        systemSize = 3480
        delta = 1560
        polymerLen = 192
    elif systemName == 'segregated':
        s = '1st conf/segregated/300K/'
        folders = [s + '1st wiggle cycle (1414047)/',
                   s + '2nd wiggle cycle (1426324)/',
                   s + '3rd wiggle cycle ok (1427860)/',
                   s + '4th wiggle cycle after corrupted (1427697)/',
                   s + '5th wiggle cycle (1428078)/',
                   s + '6th wiggle cycle (1432422)/',
                   s + '7th cycle wiggle (1440140)/']
        polymerChainsNum = 90
        chainPerCell = 10
        systemSize = 3480
        delta = 1560
        polymerLen = 192
    elif systemName == 'PA6x20':
        s = 'PA6x20/'
        folders = [s + '2024799/',]
        polymerChainsNum = 144
        chainPerCell = 144
        polymerLen = 382
    elif systemName == '5x20':
        s = 'BiggerSystems/Comp/5chains/2.1 - Slow cooling (small)/'
        folders = [s + '1795407 - wiggle no dumps/',
                   s + '1797475 - wiggle 1',
                   s + '1799268 - wiggle2',
                   s + '1808725 - wiggle3']
        polymerChainsNum = 45
        chainPerCell = 5
        systemSize = 3470
        delta = 1560
        polymerLen = 382
    elif systemName == '10x20':
        s = 'BiggerSystems/Comp/10chains/2.2 - More relaxation 500 (wiggle)/'
        folders = [s + '1795426 - wiggle no dumps/',
                   s + '1797474 - wiggle 1/',
                   s + '1799293 - wiggle2/',
                   s + '1808726 - wiggle3/']
        polymerChainsNum = 90
        chainPerCell = 10
        systemSize = 1560 + 3820
        delta = 1560
        polymerLen = 382
    else:
        folders = None
    if systemName == 'PA6x20':
        bottom = top = 0
    else:
        [bottom, top] = clayRanges(systemName)
    for folder in folders:
        fname = mainFolder + folder + 'co.50000.data'
        dp = DataParser(fname)
        dp.parseAtoms()
        atoms = dp.atoms()
        bounds = [dp.xlo(), dp.xhi(), dp.ylo(), dp.yhi(), dp.zlo(), dp.zhi()]
        zlo = dp.zlo()
        lz = dp.zhi() - zlo
        ave_rx = 0
        ave_ry = 0
        ave_rz = 0
        ove_errx = 0
        ove_erry = 0
        ove_errz = 0
        thickness = int((dp.zhi() - dp.zlo() + 1) * multiplier)
        profile = [[0, 0, 0, 0] for i in range(thickness)]
        for molNum in range(polymerChainsNum):
            if systemName in ['PA6x20',]:
                startAtomNum = (molNum % chainPerCell) * polymerLen + 1
            else:
                startAtomNum = ((molNum // chainPerCell) * systemSize + delta + (molNum % chainPerCell) * polymerLen) + 1
            molecule = makeMolecule(atoms, bounds, startAtomNum, polymerLen)
            printMolecule(molecule, molNum)
            z = 0
            atomsNum = 0
            for atom in molecule:
                atomsNum += 1
                z += atom[3]
            z /= atomsNum
            z = int(min(abs(z - top),
                        abs(z - top + lz),
                        abs(bottom + lz - z),
                        abs(bottom - z)) * multiplier)
            #print(atomsNum)
            [rx, ry, rz, errx, erry, errz] = computeRGyr(molecule)
            #profile[int((z - zlo) * multiplier)][0] += 1
            #profile[int((z - zlo) * multiplier)][1] += rx
            #profile[int((z - zlo) * multiplier)][2] += ry
            #profile[int((z - zlo) * multiplier)][3] += rz
            profile[z][0] += 1
            profile[z][1] += rx
            profile[z][2] += ry
            profile[z][3] += rz
            ave_rx += rx
            ave_ry += ry
            ave_rz += rz
            ove_errx += errx
            ove_erry += erry
            ove_errz += errz
    for valNum, val in enumerate(profile):
        if val[0] == 0:
            continue
        print(valNum / multiplier,
              val[1] / val[0],
              val[2] / val[0],
              val[3] / val[0])
            
    #print((ave_rx / polymerChainsNum)**0.5, ' +- ',
    #      (ove_errx / polymerChainsNum)**0.5, '\n',
    #      (ave_ry / polymerChainsNum)**0.5, ' +- ',
    #      (ove_erry / polymerChainsNum)**0.5, '\n',
    #      (ave_rz / polymerChainsNum)**0.5, ' +- ',
    #      (ove_errz / polymerChainsNum)**0.5)

gyration()
