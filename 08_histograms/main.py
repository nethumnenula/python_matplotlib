import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Histograms = A visual representation of the distribution of quantitative data.
#              They group values into bins (intervals)
#              and count how many fall in each range.

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100) # clip between 0 and 100

plt.hist(scores,
         bins=10,
         color="orange",
         edgecolor="black")

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("# of Students")
plt.show()