import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-1000,100,0.1)
y = np.log(x + 10)
plt.plot(x, y)
plt.show()
