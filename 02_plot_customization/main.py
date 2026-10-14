import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 22])
y2 = np.array([17, 22, 39, 8])
y3 = np.array([27, 22, 12, 32])

line_style = dict(marker=".",
                  markersize=20,
                  markerfacecolor="#6AEC58",
                  markeredgecolor="#6AEC58",
                  linestyle="solid",  # dotted, dashdot, None, dashed
                  linewidth="3")

plt.plot(x, y1, color="red", **line_style)

plt.plot(x, y2, color="yellow", **line_style)

plt.plot(x, y3, color="blue", **line_style)
plt.show()
