import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories = np.array(["Freshman", "Sophomores", "Juniors", "Seniors"])
values = np.array(([300, 250, 277, 230]))
colors = ["red", "yellow", "blue", "green"]

plt.pie(values,
        labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0, 0, 0, 0.1],
        shadow=True,
        startangle=180)

plt.title("School 1234")

plt.show()