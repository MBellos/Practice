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

#Jons marks
j_m  = df.iloc[0,2]
j_p = df.iloc[0,3]
j_c = df.iloc[0,4]

#Freds marks
f_m  = df.iloc[1, 2]
print(f_m)
f_p = df.iloc[2, 3]
print(f_p)
#f_c = df.iloc[]













#plt.bar("Mary", dfp, color = 'green', label = 'Physics Marks')
#plt.bar("Mary", dfp, color = 'orange', label = 'Maths Marks')
#plt.bar("Mary", dfp, color = 'red', label = 'Chemistry Marks')

plt.title("Marks of all students ")
plt.xlabel("Students")
plt.ylabel("Total marks")
#plt.legend()
#plt.show()
