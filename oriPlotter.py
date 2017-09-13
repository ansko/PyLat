import numpy as np
import matplotlib.pyplot as plt

xb = []
xa = []
b = []
a = []
x = []
y = []

f = open('bonds.log', 'r')
for line in f:
    ls = line.split()
    xb.append(float(ls[0]))
    b.append(float(ls[1]))


f = open('angles.log', 'r')
for line in f:
    ls = line.split()
    xa.append(float(ls[0]))
    a.append(float(ls[1]))

f = open('dp10x20.log', 'r')
for line in f:
    ls = line.split()
    x.append(float(ls[0])-9)
    y.append(float(ls[1]))


plt.figure(1)

plt.subplot(311)
red_dot, = plt.plot(xb, b, 'k-')
axes = plt.gca()
axes.set_xlim([0, 27])
axes.set_ylim([-0.2, 0.9])
plt.legend([red_dot], ["Bonds"])

plt.subplot(312)
white_cross, = plt.plot(xa, a, 'k-')
axes = plt.gca()
axes.set_xlim([0, 27])
axes.set_ylim([-0.2, 0.9])
plt.legend([red_dot], ["Angles"])

plt.subplot(313)
plt.plot(x, y, 'k-')

plt.subplots_adjust(wspace=0, hspace=0)

axes = plt.gca()
axes.set_xlim([0, 27])
axes.set_ylim([0, 2.9])

plt.legend([red_dot], ["Density profile"])


plt.suptitle('Main title')
plt.show()
