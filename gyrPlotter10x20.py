import numpy as np
import matplotlib.pyplot as plt


x = []
Rx = []
Ry = []
Rz = []
Rpoly = 9.60

f = open('gyr10x20.log', 'r')
for line in f:
    ls = line.split()
    x.append(float(ls[0]))
    Rx.append(float(ls[1]))
    Ry.append(float(ls[2]))
    Rz.append(float(ls[3]))

yBul = [1.03 for i in range(len(x))]

fig, ax = plt.subplots()
line1, = ax.plot(x, Rx, 'k<', linewidth=1,
                 label='Rx')
line2, = ax.plot(x, Ry, 'k>', linewidth=3,
                 label='Ry')
line3, = ax.plot(x, Rz, 'k^', linewidth=1,
                 label='Rz')
line5, = ax.plot([min(x), max(x)], [Rpoly, Rpoly], 'k--', linewidth=1,
                 label='Pure polymer')

ax.legend(loc='upper right', numpoints=1)

plt.xlabel(r'Distance from clay surface, $\AA$')
plt.ylabel(r'Average gyration radii, $\AA$')
axes = plt.gca()
#axes.set_xlim([0, 63])
axes.set_ylim([0, 15])
plt.show()
