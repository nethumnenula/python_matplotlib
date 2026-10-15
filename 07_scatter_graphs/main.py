import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # Hours studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # Grades

x2 = np.array([0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8]) # Hours studied
y2 = np.array([50, 60, 65, 62, 70, 70, 78, 80, 82, 92, 95])

plt.scatter(x1, y1,
            color="green",
            alpha=0.5,
            s=200,
            label="Class A")
plt.scatter(x2, y2,
            color="red",
            alpha=0.5,
            s=200,
            label="Class B")

plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.title("Test Score",
          color="Green",
          fontweight="bold")
plt.legend()
plt.show()