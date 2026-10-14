import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 22])
y2 = np.array([17, 22, 39, 8])
y3 = np.array([27, 22, 12, 32])

plt.title("Class Size",
          fontsize=20,
          family="Arial",
          fontweight="bold",
          color="red")

plt.xlabel("Year",
           fontsize=15,
           family="Arial",
           #fontweight="bold",
           color="blue",)
plt.ylabel("Students",
           fontsize=15,
           family="Arial",
           #fontweight="bold",
           color="blue",)

plt.tick_params(axis="both", colors="blue")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()
