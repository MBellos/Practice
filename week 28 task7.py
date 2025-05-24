import pandas as pd
from matplotlib import pyplot as plt

data_dict = {
    'name': ['Jon', 'Fred', 'Mary', 'Sue', 'Kim', 'Sally'],
    'age': [20, 20, 21, 20, 21, 20],
    'maths_marks': [100, 90, 91, 98, 92, 95],
    'physics_marks': [90, 100, 91, 92, 98, 95],
    'chemistry_marks': [93, 89, 99, 92, 94, 92]
}

df = pd.DataFrame(data_dict)

df1 = (df["physics_marks"].sort_values(ascending = True))
plt.plot(df1)
plt.show()
