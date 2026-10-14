import matplotlib.pyplot as plt
import numpy as np

# grid() = Helps make plots easier to read by adding reference lines.

x = np.array([1, 2, 3, 4, 5])
y = x * 5

plt.grid(axis="both", linewidth=2,
         color="lightgray",
         linestyle="solid")


plt.plot(x, y)
plt.xticks(x)
plt.yticks(y)
plt.show()