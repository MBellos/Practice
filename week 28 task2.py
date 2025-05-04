import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("lw.csv")

length = df.filter(items=['Length'])
width = df.filter(items=['Width'])
print(width)
print(length)

plt.plot(length, label = 'Length')
plt.plot(width, label = 'Width')
plt.legend()
plt.show()
