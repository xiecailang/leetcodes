import matplotlib.pyplot as plt
import numpy as np
mu, gama = 0,0.5
x = np.arange(-10, 10, 0.01)
f = np.divide(np.e**(-(x - mu)/gama), gama*(1+np.e**(-(x - mu)/gama))**2)
F = 1/(1+np.e**(-(x - mu)/gama))
plt.plot(x, f)
plt.plot(x, F)
plt.show()