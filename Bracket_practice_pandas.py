#Practicing using brackets correctly when working with loc and iloc (pandas)
import pandas as pd
from matplotlib import pyplot as plt

#Reading csv file
df = pd.read_csv("Rainfall_2000_2004.csv")

#Access all the values in April column #1 - FAIL 
#df_column = df.loc['Apr']
#print(df_column)

#Access all the values in April column #2 - PASS - use : to say "all rows" followed by column name
df_april = df.loc[:,'Apr']
print(df_april)

