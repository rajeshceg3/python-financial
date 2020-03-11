import matplotlib.pyplot as plt
import numpy as np

mean, sd = 0, 1
s = np.random.normal(mean, sd, 1000)
plt.hist(s, 35, density=True)
plt.show()
