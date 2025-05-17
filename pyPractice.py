import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime




df = pd.read_csv("Rainfall_2000_2004.csv")

#Attempting to validate/format date from user_input

def get_date():
    Flag = True
    while Flag:
        user_date = input("Please enter a date, in the format DD/MM/YYYY: ")
        try:
            date_format =  "%d/%m/%Y"
            format_date = datetime.strptime(user_date, date_format)
        except:
            print("You did not enter in the right format, please try again.")
        else:
            print("Date accepted!")
            Flag = False
    return format_date

date = get_date()
