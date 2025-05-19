#Sorting files in python pandas
from matplotlib import pyplot as plt
import pandas as pd

#df = pd.read_csv("Task4a_data.csv")

#df1 = df.sort_values(by ='Menu Item', ascending=True)# format is dataframe.sort_values(by='', ascending=True/False)
#print(df1)

#-------------------------------------------------------------------------------------------------------------------

#Finding unique values in a dataset (csv)

#unique_menu_items = df['Menu Item'].unique().tolist()# tolist() - turns output into a list of the unique values
#print(unique_menu_items)

#unique_items = df['Menu Item'].nunique()
#print(unique_items)

#------------------------------------------------------------------------------------------------------------------

#Using Value_counts() to find the unique type of values

#menu_values = df.loc['Menu Item'].value_counts()
#print(menu_values)

#------------------------------------------------------------------------------------------------------------------

#Filtering based on 2 columns

df5 = pd.read_csv('Rainfall_2000_2004.csv')

city_and_june = df5.loc[df5['City'] == 'London', 'Jun'].sum()
print(f"The amount of total rainfall in London in the month of June is {city_and_june}.")
















