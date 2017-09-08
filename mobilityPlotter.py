import numpy as np
import matplotlib.pyplot as plt


x = []
y = []
f = open('mobility.log', 'r')
for line in f:
    ls = line.split()
    x.append(float(ls[0]))
    y.append(float(ls[1]))

fig, ax = plt.subplots()
line1, = ax.plot(x, y, 'k^', linewidth=1,
                 label='Atomic displacements')

ax.legend(loc='lower right', numpoints=1)
plt.show()
