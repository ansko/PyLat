import numpy as np
import matplotlib.pyplot as plt


plt.figure(1)

plt.subplot(311)
plt.plot([1, 2, 3, 4], [2, 2, 2, 2], 'r-')

plt.subplot(312)
plt.plot([1, 2, 3, 4], [3, 3, 3, 3], 'r-')

plt.subplot(313)
plt.plot([1, 2, 3, 4], [3, 3, 3, 3], 'r-')

plt.subplots_adjust(wspace=0, hspace=0)

plt.show()
