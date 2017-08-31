#!/usr/bin/env python3
# coding utf-8

import pprint
pprint=pprint.PrettyPrinter(indent=1).pprint

from Classes.DataParser import DataParser
from Classes.Options import Options


def atomicMobility(T=300):
    o = Options()
    systemName = o.getProperty('systemName')
    multiplier = o.getProperty('multiplier')
    mainFolder = o.getProperty('mainFolder')
    if systemName == 'mixed':
        if T == 300:
            s = '1st conf/mixed ok/300K/relaxation+wiggle/'
            startFile =  mainFolder + s + '1st wiggle cycle (1414048 )/co.50000.data'
            endFile =  mainFolder + s + '7th wiggle cycle (1455489)/co.2500000.data'
        else:
            startFile = None
            endFile = None
    elif systemName == 'segregated':
        if T == 300:
            s = '1st conf/segregated/300K/'
            startFile =  mainFolder + s + '1st wiggle cycle (1414047)/co.50000.data'
            endFile =  mainFolder + s + '6th wiggle cycle (1432422)/co.2500000.data'
    elif systemName == 'PA6x20':
        if T == 300:
            s = 'PA6x20/2024799/'
            startFile = mainFolder + s + 'co.50000.data'
            endFile = mainFolder + s + 'co.7500000.data'
        else:
            startFile = None
            endFile = None
            
    dpStart = DataParser(startFile)
    dpStart.parseAtoms()
    startAtoms = dpStart.atoms()
    dpEnd = DataParser(endFile)
    dpEnd.parseAtoms()
    endAtoms = dpEnd.atoms()
    masses = dpStart.masses()
    lx = dpStart.xhi() - dpStart.xlo()
    ly = dpStart.yhi() - dpStart.ylo()
    lz = dpStart.zhi() - dpStart.zlo()
    zlo = dpStart.zlo()
    thickness = int((dpStart.zhi() - dpStart.zlo() + 1) * multiplier)
    profile = [[0, 0] for i in range(thickness)]
    for atomNum, atom in enumerate(startAtoms):
        if atomNum == 0:
            continue
        if masses[atom[1]] < 2:
            continue
        x0 = atom[3]
        y0 = atom[4]
        z0 = atom[5]
        x1 = endAtoms[atomNum][3]
        y1 = endAtoms[atomNum][4]
        z1 = endAtoms[atomNum][5]
        dx = min(abs(x1 - x0), abs(lx - abs(x1 - x0)))
        dy = min(abs(y1 - y0), abs(ly - abs(y1 - y0)))
        dz = min(abs(z1 - z0), abs(lz - abs(z1 - z0)))
        dr = (dx**2 + dy**2 + dz**2)**0.5
        profile[int((z0 - zlo) * multiplier)][0] += 1
        profile[int((z0 - zlo) * multiplier)][1] += dr
    for z, element in enumerate(profile):
        if element[0] == 0:
            continue
        print(z / multiplier, element[1] / element[0])
        
        
atomicMobility()