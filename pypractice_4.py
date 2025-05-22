#practice

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Task4a_data.csv')

#sorting values
df_sorted = df.sort_values(by='Menu Item', ascending = True)
#print(df_sorted)

#Grouping values and finding the highest of each

df_group = df.groupby('Menu Item')['03/03/2023'].max().get('Brisket')
#print(df_group)

#Value count finding how many of smt there are

df_sorted = df.value_counts('Menu Item')
#print(df_sorted)

#Sorting mutiple values
#df_sort_multiple = df.value_counts(('Menu Item')&('Lunch Dinner'))
#print(df_sort_multiple)

#Finding highest item in row

df_high = df.iloc[6, 3:9].max()
#print(df_high)

#Finding lowest item in a row

df_low = df.iloc[6, 3:9].min()
#print(df_low)

#Finding the mean of a row

df_mn = df.iloc[6, 3:9].mean()
#print(df_mn)

#Finding the unique values of a row

df_unq = df['Menu Item'].unique().tolist()
#print(df_unq)

#Checking if user input is a string
#flag = True
#while flag:
  #  user_input = input("please enter a string of characters: ")

    #try:
        #check = isinstance(user_input, str)
      #  if check == False:
          #  print("Please enter a string!!!")
        #else:
          #  print("Thank you!!")
            #flag = False
    #except:
      #  print("Invalid input, try again.")


#display bar charts

#df_bar_din = df.loc[(df['Menu Item'] == 'Brisket')&(df['Service'] == 'Dinner')].select_dtypes('int').sum().sum()
#df_bar_lun = df.loc[(df['Menu Item'] == 'Brisket')&(df['Service'] == 'Lunch')].select_dtypes('int').sum().sum()

#plt.bar('Brisket - Din', df_bar_din, color = 'blue', label = 'Dinner')
#plt.bar('Brisket - Lun', df_bar_lun, color = 'green', label = 'Lunch')

#plt.title("The total sales for Brisket at lunch and dinner")
#plt.xlabel("Menu Item")
#plt.ylabel("Amount of sales")
#plt.legend()

#plt.show()

#displaying pie chart

df_bar_din = df.loc[(df['Menu Item'] == 'Brisket')&(df['Service'] == 'Dinner')].select_dtypes('int').sum().sum()
df_bar_lun = df.loc[(df['Menu Item'] == 'Brisket')&(df['Service'] == 'Lunch')].select_dtypes('int').sum().sum()

plot_data = [df_bar_din, df_bar_lun]
labels = ['Brisket - Dinner', 'Brisket - Lunch']
plt.pie(plot_data, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("The total sales for Brisket at lunch and dinner")
plt.show()

























