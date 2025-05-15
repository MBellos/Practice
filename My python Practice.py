#Declare Global Constant
MAX_LINES = 3
MAX_BET =100
MIN_BET = 1
#Making a Function
#A functon is call to execute a certain block of code and return a value.
def deposit():
#Responsible for collecting user input
     #setting up a while loop continually ask the user to enter an amount.
    while True: 
        amount =  input("What would you like to deposit? $")
        if  amount.isdigit ():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print ("Amount must be greater than 0 mate ;-; ")
        else:
            print("Enter a number dumbass.")
    return amount
#Another while loop to get the amount of limes to bet on. 
def get_number_of_lines():
        while True:
            lines =  input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
            if  lines.isdigit ():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print ("Enter a valid number of lines mate ;-; ")
        else:
            print("Enter a number dumbass.")
        return lines

def get_bet():
    while True: 
        amount=  input("What would you like to bet on each line? $")
        if  amount.isdigit ():
            amount = int(amount)
            if MIN_BET <=  amount  <= MAX_BET:
                break
            else:
                print("Amount must be between $" + str(MIN_BET) - str(MAX_BET) + ". mate ;-; ")
        else:
            print("Enter a number dumbass.")
    return amount
#Main Program
def main():
    balance = deposit( )#Calling the function and putting the program ("def main")into this fuction.
    lines =  get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print ("You do not have enough money to bet that amount, you current balance is: $ "+str(balance)+" You could always pay with your life >:>")
        else:
                break
    print("You are betting $"+ str(bet) +" on "+ str(lines) +" lines. Total bet is equal to: $"+ str(total_bet) +".")

main() 
 
   
 
