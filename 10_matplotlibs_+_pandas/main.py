import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("pokemon.csv")

# print(df.to_string())

print(df["Type 1"].value_counts())

type_count = df["Type 1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values,
         color="orange",
         edgecolor="black")

plt.title("Number of Pokemon by type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.show()

