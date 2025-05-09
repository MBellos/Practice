import pandas as pd
from matplotlib import pyplot as plt

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show total sales for a specific item during lunch and dinner")
        print("3. Show total sales for two items during lunch and dinner")
        #print("4. Show the highest menu total and average")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name
            
#Getting the second item choice for comparison graphs
#Menu item selection form user and validates it
def get_product_choice2():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose another menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")

        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name
            
#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date


#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date

#imports data set and extracts data for a specific menu item between lunch and dinner within a user defined range
#displaying a bar chart with this information
def get_lunch_dinner(order_item, start_date2, end_date2):
    df = pd.read_csv("Task4a_data.csv")
    df1 = df.loc[df['Menu Item'] == order_item]
    
    df2 = df1.loc[:,start_date2:end_date2]

    
#Filtering the dataframe based on the service type
    lunch_sum = df2.loc[(df['Service'] == "Lunch") & (df['Menu Item'] == order_item)].select_dtypes('int').sum().sum()
    dinner_sum = df2.loc[(df['Service'] == "Dinner") & (df['Menu Item'] == order_item)].select_dtypes('int').sum().sum()

    lunch_mean = df2.loc[(df['Service'] == "Lunch") & (df['Menu Item'] == order_item)].select_dtypes('int').mean().mean()
    dinner_mean = df2.loc[(df['Service'] == "Dinner") & (df['Menu Item'] == order_item)].select_dtypes('int').mean().mean()
    lunch_mean = lunch_mean.round(1)
    dinner_mean = dinner_mean.round(1)

    
#Plotting bar chart to show difference between the lunch and dinner sales of the order item entered
#Genereating text description of bar chart and averages
    lunch_label = str(f"{order_item} - Lunch")
    dinner_label = str(f"{order_item} - Dinner")

    print("\nHere is the sales data for {} between dates {} and {}:".format(order_item, start_date2, end_date2))
    print(f"***************************\nThe total lunch sales for {order_item} total to: {lunch_sum}\n***************************\n\n***************************\nThe total dinner sales for {order_item} total to: {dinner_sum}\n***************************\n")
    print(f"***************************\nThe average lunch sales for {order_item} is: {lunch_mean}\n***************************\n\n***************************\nThe average dinner sales for {order_item} is: {dinner_mean}\n***************************") 
    plt.bar(lunch_label, lunch_sum, color = "red", label = "Lunch")
    plt.bar(dinner_label, dinner_sum, color = "blue", label = "Dinner")
    plt.title(f"Difference Betweeen Lunch and Dinner Sales of {order_item}")
    
    plt.xlabel(f"Service Type and Menu Item: {order_item}")
    plt.ylabel(f"Amount of Sales {start_date2} - {end_date2}")
    plt.legend()
    plt.show()

 
    return df2 
    
#Plotting bar chart to show the difference between the total and averages of two menu items between lunch and dinner
#Imports data set and extracts data and returns data for two specific menu items within a user defined range
def get_item_difference(item_choice1, item_choice2, start_date3, end_date3):
    df = pd.read_csv("Task4a_data.csv")
    df1 = df.loc[df['Menu Item'] == item_choice1]
    df2 = df.loc[df['Menu Item'] == item_choice2]
    choice1_dates = df1.loc[:,start_date3:end_date3]
    choice2_dates = df2.loc[:,start_date3:end_date3]
    
#Lunch and dinner totals for the first menu item the user chooses
    lunch_sum_choice1 = choice1_dates.loc[(df['Service'] == "Lunch") & (df['Menu Item'] == item_choice1)].select_dtypes('int').sum().sum()
    dinner_sum_choice1 = choice1_dates.loc[(df['Service'] == "Dinner") & (df['Menu Item'] == item_choice1)].select_dtypes('int').sum().sum()

    lunch_sum_choice2 = choice2_dates.loc[(df['Service'] == "Lunch") & (df['Menu Item'] == item_choice2)].select_dtypes('int').sum().sum()
    dinner_sum_choice2 = choice2_dates.loc[(df['Service'] == "Dinner") & (df['Menu Item'] == item_choice2)].select_dtypes('int').sum().sum()
    
#Lunch and dinner averages for the first and second item the user chooses
    lunch_mean_choice1 = choice1_dates.loc[(df['Service'] == "Lunch") & (df['Menu Item'] == item_choice1)].select_dtypes('int').mean().mean()
    dinner_mean_choice1 = choice1_dates.loc[(df['Service'] == "Dinner") & (df['Menu Item'] == item_choice1)].select_dtypes('int').mean().mean()

    lunch_mean_choice2 = choice2_dates.loc[(df['Service'] == "Lunch") & (df['Menu Item'] == item_choice2)].select_dtypes('int').mean().mean()
    dinner_mean_choice2 = choice2_dates.loc[(df['Service'] == "Dinner") & (df['Menu Item'] == item_choice2)].select_dtypes('int').mean().mean()
#Choice 1
    lunch_mean_choice1 = lunch_mean_choice1.round(1)
    dinner_mean_choice1 = dinner_mean_choice1.round(1)
#Choice 2
    lunch_mean_choice2 = lunch_mean_choice2.round(1)
    dinner_mean_choice2 = dinner_mean_choice2.round(1)
    
#Plotting bar chart to show difference between the lunch and dinner sales of the order item entered
#Genereating text description of bar chart and averages
#Choice 1
    lunch1_label = str(f"{item_choice1} ")
    dinner1_label = str(f"{item_choice1}   ")
#Choice 2
    lunch2_label = str(f"{item_choice2}  ")
    dinner2_label = str(f"{item_choice2}   ")
    
    
    print("\nHere is the sales data for {} and {} between dates {} and {}:".format(item_choice1, item_choice2, start_date3, end_date3))
#Choice 1
    print(f"***************************\nThe total lunch sales for {item_choice1} total to: {lunch_sum_choice1}\nThe total dinner sales for {item_choice1} total to: {dinner_sum_choice1}\n***************************\n")
    print(f"***************************\nThe average lunch sales for {item_choice1} is: {lunch_mean_choice1}\nThe average dinner sales for {item_choice1} is: {dinner_mean_choice1}\n***************************\n")

#Choice 2
    print(f"***************************\nThe total lunch sales for {item_choice2} total to: {lunch_sum_choice2}\nThe total dinner sales for {item_choice2} total to: {dinner_sum_choice1}\n***************************\n")
    print(f"***************************\nThe average lunch sales for {item_choice2} is: {lunch_mean_choice2}\nThe average dinner sales for {item_choice2} is: {dinner_mean_choice2}\n***************************")


#Choice 1  
    plt.bar(lunch1_label, lunch_sum_choice1, color = "orange", label = "Lunch")
    plt.bar(dinner1_label, dinner_sum_choice1, color = "green")
#Choice 2   
    plt.bar(lunch2_label, lunch_sum_choice2, color = "orange")
    plt.bar(dinner2_label, dinner_sum_choice2, color = "green", label = "Dinner")
    
    plt.title(f"Difference Betweeen Lunch and Dinner Sales of {item_choice1} and {item_choice2}")
    plt.xlabel(f"Service Type and Menu Item: {item_choice1} and {item_choice2}")
    plt.ylabel(f"Amount of Sales {start_date3} - {end_date3}")
    plt.legend()
    plt.show()


    return choice1_dates, choice2_dates


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

     
main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)
    print(extract_no_index)
    
elif main_menu == 2:
    order_item = get_product_choice()
    start_date2 = get_start_date()
    end_date2 = get_end_date()
    lunch_dinner_bar = get_lunch_dinner(order_item, start_date2, end_date2)
    
elif main_menu == 3:
    item_choice1 = get_product_choice()
    item_choice2 = get_product_choice2()
    start_date3 = get_start_date()
    end_date3 = get_end_date()
    two_item = get_item_difference(item_choice1, item_choice2, start_date3, end_date3)
    
#elif main_menu == 4:
    #start_date4 = get_start_date()
    #end_date4 = get_end_date()
    #highest_item = high_menu_item(start_date4, end_date4)
   
else:
    print('This part of the program is still under development')











