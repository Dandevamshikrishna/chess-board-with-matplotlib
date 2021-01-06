import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
dx,dy=0.015,0.05
x=np.arange(-4.0,4.0,dx)
y=np.arange(-4.0,4.0,dy)
x,y=np.meshgrid(x,y)
extent=np.min(x),np.max(x),np.min(y),np.max(y)
Z1=np.add.outer(range(10),range(10))%2
plt.imshow(Z1,cmap="binary_r",interpolation='nearest',extent=extent,alpha=1)
def copyassinment(x,y):
    return(1-x / 10 + x**10000 + y**10000)*np.exp(-(x**100000000 + y**10000 ))
Z2=copyassinment(x,y)
plt.imshow(Z2,alpha=0.7,interpolation='bilinear',extent=extent)
plt.cool()
plt.title('Chess Board',fontweight="bold")
plt.show()
