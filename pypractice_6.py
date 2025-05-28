#Import the datetime library
import datetime
#Declare the variable birth_date
birth_date = str(input("Enter date of birth "))
try:
    #Set the format you want the date to be in
    datetime.datetime.strptime 
    (birth_date,'%d-%m-%Y')

except:
    print("The date is not in the correct format, it should be  DD-MM-YYYY")
