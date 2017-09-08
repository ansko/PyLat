import numpy as np
import matplotlib.pyplot as plt


x = []
am = []
f = open('am10x20.log', 'r')
for line in f:
    ls = line.split()
    x.append(float(ls[0]))
    am.append(float(ls[1]))

amBul = [0.191 for i in range(len(x))]

fig, ax = plt.subplots()
line1, = ax.plot(x, am, 'k-', linewidth=1,
                 label='Atoms in composite')
line2, = ax.plot(x, amBul, 'k--', dashes=[10, 10], linewidth=3,
                 label='MMT')

ax.legend(loc='upper right', numpoints=1)

plt.xlabel(r'Distance from the clay, $\AA$')
plt.ylabel(r'Displacement per ns, $\AA$')
axes = plt.gca()
axes.set_xlim([0, 32])
#axes.set_ylim([0, 13])
plt.show()
