import pandas as pd
from matplotlib import pyplot as plt

#Opening csv for reading
df = pd.read_csv("Rainfall_2000_2004.csv")

#Attempting to only show values in London 1 - PASS
london_df = df.loc[df['City'] == 'London']
#print(london_df)

#Attempting to only show values in March 1 - PASS
march_df = df.loc[:,'Mar']
#print(march_df)

#Attempting to only show values from London and March - FAIL
lon_mar_df = df.loc[df['City'] == 'London', 'Mar']#meaning - df.loc[df['row'] == 'row_name', 'column']
#print(lon_mar_df)

#Attempting to only show row and/or column that is searched for by user
print("Years\n*******************\n2000-2004\n")#Years available
row_srch1 = input ("Please enter a year to search: \n")

print("Cities\n*******************\nLondon\nBirmingham\nLeeds\nManchester")
row_srch2 = input ("Please enter a city to search: \n")#Cities available
row_srch2 = row_srch2.capitalize()

print("Months\n*******************\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec")#Months available
col_srch = input("Please enter a Month to search: \n")
col_srch = col_srch.capitalize()

user_row = df.loc[(df['City'] == row_srch2) & (df['Year'] == row_srch1), col_srch]
print(user_row)









#\n
