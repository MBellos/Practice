import pandas as pd
from matplotlib import pyplot as plt

# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. Total income by payment type")
        print("### 3. Income sources - pie chart")
        print("### 4. Income by day of the week")

        

        choice = input('Enter your number selection here: ')
        men_options = ["1","2","3", "4"]

        if choice == "": #Checking if the user entered any input and if not display error message and looping back to menu
                print("Nothing was entered, please enter valid input")
                flag = True

        try:
            int(choice)#Checking if the user input can be changed into a integer
    
            if choice not in  men_options:
                print("Please pick an option from the menu using the menu numbers")

            else:
                print('Choice accepted!')
                flag = False
        except:
            print("Sorry, you did not enter a valid option")
            flag = True  


    return choice

# Submenu for totals, provides type check validation for the input
def total_menu ():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total income by source ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Tickets")   
        print("### 2. Gift Shop") 
        print("### 3. Snack Stand")  
        print("### 4. Pictures")


        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True

        if choice == " ": #Checking if the user entered any input and if not display error message and looping back to menu
            print("Nothing was entered, please enter valid input")
            flag = True
        
        else:    
            print('Choice accepted!')
            flag = False
            

    return choice   

# takes the total submenu input and converts the number to a string of the source name
def convert_total_men_coice(total_men_choice):
    
    if total_men_choice == "1":
        tot_choice = "Tickets"
        
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
        
    elif total_men_choice == "3":
        tot_choice= "Snack Stand"
    else:
        tot_choice = "Pictures"  
    
    return tot_choice

# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    
    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg

#Creates bar chart to show the cash and card sales differences
#outputs in text and a bar graph
def payment_type_bar():
    
    df = pd.read_csv("Task4a_data.csv")
    
#Separating the data from the income sources into separate dataframes for cash and card
    sales_columns = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]
    
    df_cash = df.loc[df['Pay Type'] == 'Cash', sales_columns].sum().sum()
    df_card = df.loc[df['Pay Type'] == 'Card', sales_columns].sum().sum()
    
#Generating text description of data
    print("########## Test Description ##########")
    print(f"The total cash sales from all income sources is £{df_cash}")
    print(f"The total card sales from all income sources is £{df_card}")
    print(f"The difference between the cash and card sales is £{df_card - df_cash}")
    
#Plotting a bar graph in a user friendly way
    plt.bar("Cash", df_cash, color = ['red'], label = ['Cash sales'])
    plt.bar("Card", df_card, color = ['green'], label = ['Card sales'])
    plt.title("Income by Payment Type")
    plt.xlabel("Payment Types")
    plt.ylabel("Total income (£)")
    plt.legend()
    
    plt.show()

#Creating pie chart of all income sources
def inc_source_pie():
    df = pd.read_csv("Task4a_data.csv")
    
#Creating new dataframes for all the income sources and adding the togeth
    tot_tickets = df[['Tickets']].select_dtypes('int').sum().sum()
    tot_gift_shop = df[['Gift Shop']].select_dtypes('int').sum().sum()
    tot_snack_stand= df[['Snack Stand']].select_dtypes('int').sum().sum()
    tot_pictures = df[['Pictures']].select_dtypes('int').sum().sum()
    
    labels = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]
    values = [tot_tickets, tot_gift_shop, tot_snack_stand, tot_pictures]

    plt.pie(values, labels = labels, autopct='%1.1f%%', startangle = 90)
    plt.title("Revenue from Income Sources")
    plt.axis("equal")
    plt.show()

def inc_source_bar():
    df = pd.read_csv("Task4a_data.csv")
    sales_columns = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]
    
#Creating new dataframes for all the income sources and adding the together
    tot_tickets = df[['Tickets']].select_dtypes('int').sum().sum()
    tot_gift_shop = df[['Gift Shop']].select_dtypes('int').sum().sum()
    tot_snack_stand = df[['Snack Stand']].select_dtypes('int').sum().sum()
    tot_pictures = df[['Pictures']].select_dtypes('int').sum().sum()
 
    
#Creating bar chart of all income sources
    plt.bar("Tickets", tot_tickets, color = 'red', label = 'Ticket sales')
    plt.bar("Gift Shop", tot_gift_shop, color = 'yellow', label = 'Gift Shop')
    plt.bar("Snack Stand", tot_snack_stand, color = 'pink', label = 'Stack Stand')
    plt.bar("Pictures", tot_pictures, color = 'orange', label = 'Pictures')
    plt.legend()
    plt.title("Revenue from Income Sources")
    plt.xlabel("Income Sources")
    plt.ylabel("Total Incomes (£)")
    plt.show()


#Creating a menu to choose from bar or pie chart for better usability
def income_source_graph():
    flag = True
    print("####################################################")
    print("#### Graphical representaions of income sources ####")
    print("####################################################")
    print("")
    print("########## Please select a graph ##########")
    print("### 1. Bar Graph")   
    print("### 2. Pie Chart")

    while flag:
        choice = input("Please enter an option: ")
        men_options = ["1", "2"]


        if choice == "": #Checking if the user entered any input and if not display error message and looping back to menu
            print("Nothing was entered, please enter valid input")
            flag = True

        try:
            int(choice)#Checking if the user input can be changed into a integer
        
            if choice not in  men_options:
                print("Please pick an option from the menu using the menu numbers")

            else:
                print('Choice accepted!')
                flag = False
        except:
            print("Sorry, you did not enter a valid option")
            flag = True

        if choice == "1":
            inc_source_bar()
            
        elif choice == "2":
            inc_source_pie()
            
def inc_per_day():
    df = pd.read_csv("Task4a_data.csv")

#Finding the average sales of mondays
    inc_monday = df[df['Day'] == 'Monday'].select_dtypes('int').mean().sum()
    print(f"The average income generated on Monday's £{inc_monday}")
    
#Finding the average sales of tuesday
    inc_tuesday = df[df['Day'] == 'Tuesday'].select_dtypes('int').mean().sum()

    print(f"The average income generated on Tuesday's £{inc_tuesday}")
    
#Finding the average sales of wednesday
    inc_wednesday = df[df['Day'] == 'Wednesday'].select_dtypes('int').mean().sum()

    print(f"The average income generated on wednesday's £{inc_wednesday}")
    
#Finding the average sales of thursday
    inc_thursday = df[df['Day'] == 'Thursday'].select_dtypes('int').mean().sum()

    print(f"The average income generated on Thursday's £{inc_thursday}")
    
#Finding the average sales of friday
    inc_friday = df[df['Day'] == 'Friday'].select_dtypes('int').mean().sum()

    print(f"The average income generated on Friday's £{inc_friday}")
    
#Finding the average sales of saturday
    inc_saturday = df[df['Day'] == 'Saturday'].select_dtypes('int').mean().sum()

    print(f"The average income generated on Saturday's £{inc_saturday}")
    
#Finding the average sales of sunday
    inc_sunday = df[df['Day'] == 'Sunday'].select_dtypes('int').mean().sum()

    print(f"The average income generated on Sunday's £{inc_sunday}")

#Genertaing bar chart for the average income for each day of the week
    plt.bar("Mon", inc_monday, color = 'red', label = 'Monday sales')
    plt.bar("Tues", inc_tuesday, color = 'green', label = 'Tuesday sales')
    plt.bar("Wed", inc_wednesday, color = 'yellow', label = 'Wednesday sales')
    plt.bar("Thur", inc_thursday, color = 'pink', label = 'Thursday sales')
    plt.bar("Fri", inc_friday, color = 'blue', label = 'Friday sales')
    plt.bar("Sat", inc_saturday, color = 'orange', label = 'Saturday sales')
    plt.bar("Sun", inc_sunday, color = 'purple', label = 'Sunday sales')

    plt.title("Average Income Generated per day of the week")
    plt.xlabel("Days of the week")
    plt.ylabel("Average Income (£)")
    plt.legend()
    plt.show()

    


    

#Checking what option the user picked from main_menu and referenceing and calling back to necessary subprograms
main_menu_choice = main_menu()
#Menu choice 1
if main_menu_choice == "1":
    total_men_choice = total_menu()
    total_choice = convert_total_men_coice(total_men_choice)
    print(get_total_data(total_choice))
    
#Menu choice 2
elif main_menu_choice == "2":
    payment_type_bar()

#Menu choice 3
elif main_menu_choice == "3":
    income_source_graph()

#Menu choice 4
elif main_menu_choice == "4":
    inc_per_day()
    







    










    
