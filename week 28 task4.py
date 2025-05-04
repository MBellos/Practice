import pandas as pd
from matplotlib import pyplot as plt

data = {
        "calories": [420,380,390],
        "duration": [50,40,45]
        }

#load data into Datafram object:
df = pd.DataFrame(data)
df.plot()
plt.show()
