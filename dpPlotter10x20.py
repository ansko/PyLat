import numpy as np
import matplotlib.pyplot as plt


x = []
yAll = []
yMMT = []
yMod = []
yPol = []
f = open('dp10x20.log', 'r')
for line in f:
    ls = line.split()
    x.append(float(ls[0]))
    yAll.append(float(ls[1]))
    yMMT.append(float(ls[2]))
    yMod.append(float(ls[3]))
    yPol.append(float(ls[4]))

yBul = [1.03 for i in range(len(x))]

fig, ax = plt.subplots()
line1, = ax.plot(x, yAll, 'k-', linewidth=1,
                 label='All atoms')
line2, = ax.plot(x, yMMT, 'k--', dashes=[1, 1], linewidth=3,
                 label='MMT')
line3, = ax.plot(x, yMod, 'k--', dashes=[2, 2], linewidth=1,
                 label='Modifier')
line4, = ax.plot(x, yPol, 'k--', dashes=[5, 5], linewidth=1,
                 label='Polymer')
line5, = ax.plot(x, yBul, 'k--', dashes=[10, 10], linewidth=1,
                 label='Pure polymer')

ax.legend(loc='upper right', numpoints=1)

plt.xlabel(r'Distance along z, $\AA$')
plt.ylabel(r'Density, $g/cm^3$')
axes = plt.gca()
axes.set_xlim([0, 63])
axes.set_ylim([0, 13])
plt.show()
