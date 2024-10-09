import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
sin = np.load('task7_sin.npy')
cos = np.load('task7_cos.npy')
plt.plot(x,sin, color="blue")
plt.plot(x,cos,color = "orange")
plt.show()
