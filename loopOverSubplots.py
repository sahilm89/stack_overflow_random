import matplotlib.pyplot as plt
import numpy as np
#data
x = np.linspace(0, 2 * np.pi, 400)

y = [np.sin(x), np.sin(x**2), np.cos(x**2)]
title = ['y1','y2','y3']

#plot       
numPlots = len(y)
f = plt.figure()
ax = []
for i in range(numPlots):
    ax.append(f.add_subplot(numPlots,1,i+1))
    ax[i].plot(x, y[i])
    ax[i].set_title(title[i])
    f.subplots_adjust(hspace=0.3)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.show()
