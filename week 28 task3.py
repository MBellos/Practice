#Week 28 Task2

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("lw.csv")

L_merc = df.loc[0, "Length"]
W_merc = df.loc[0, "Width"]


L_ford = df.loc[1, "Length"]
W_ford = df.loc[1, "Width"]


L_austin = df.loc[2, "Length"]
W_austin = df.loc[2, "Width"]


plt.bar("Length M", L_merc, color = "Red", label = 'Mercedes')
plt.bar("Width M", W_merc, color = "Red", label = 'Mercedes')

plt.bar("Length F", L_ford, color = "Yellow", label = 'Ford')
plt.bar("Width F", W_ford, color = "Yellow", label = 'Ford')

plt.bar("Length A", L_austin, color = "Green", label = 'Austin')
plt.bar("Width A", W_austin, color = "Green", label = 'Austin')

plt.title("Difference between the Lengths and Width of the Cars")
plt.xlabel("Length and Widths of the cars")
plt.ylabel("Lengths (m)")
plt.legend()

plt.show()


