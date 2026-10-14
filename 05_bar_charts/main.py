import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 5, 3.3, 1])

bar_settings = dict(
    color="orange",

)

plt.bar(categories, values, **bar_settings)
# plt.barh(categories, values, **bar_settings)

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()