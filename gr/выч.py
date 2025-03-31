import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

plt.plot(x, y)
import numpy as np
# Устанавливаем деления на оси X через 0.5
plt.xticks(np.arange(min(x), max(x) + 0.5, 0.5))
plt.show()