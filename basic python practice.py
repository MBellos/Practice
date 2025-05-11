#Python Practice
#NESTED LOOPS-  a loop within another loop (outer, inner)
#                                 outer loop:
#                                     inner loop:
for x in range(3): # the outer loop in repeating the inner loop 3 time
    for y in range(1,10): # the inner loop is being repeated by the outer loop
        print(y, end=" ") # to keep the output on the same line you can use ,end=" " / OR / "-"
    print() # adding the blank print statement just adds a new line. Use this indentaion


# RECTANGLE EXAMPLE
rows = int(input("Enter the number of rows for your rectangle: "))
columns = int(input("Enter the number of columns for your rectangle: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()

#CREATING, READING AND APPENDING FILES
#WRITING TO THE FILE
#write_file = open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "w")
#To add a specific place to save the file, copy the file directory and add \ backslash
#before file name ALSO x is to create a file in the , "x" area. w is to create and write to it
#write_file.write("This is our first sentence in our file!")
#write_file.close()
#APPENDING THE FILE
#append_file = open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "a")
#append_file.write("This is our second sentence in our file!")
#append_file.close()
#Using a contact/context?? manager for better efficiency
#with open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "a") as append_file:
  #  append_file.write("\n This is our third sentence in our file on a new line!")
#append_file.close()
#READING THE FILE
#with open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "r") as read_file:
  #  print(read_file.read())
#read_file.close()
#Can add a variable for ease of use
#with open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "a") as read_file:
    #print(read_file.read())
#The three """ below is called a triple statement
multi_line = """
This is the fourth sentence.
The Fifth.
And the Sixth.
"""
with open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "w") as append_file:
    append_file.write(multi_line)
append_file.close()
with open(r"C:\Users\user\Documents\Python Files\PythonPractice3.txt", "r") as read_file:
    print(read_file.read())
read_file.close()
#THE ABOVE IS NOT WORKING CORRECTLY

#THE JOIN STRING METHOD
#Any data type that is a sequence can be iterated over
a = "-" # if the a was a - the output would be : M-C-0 if it was d the output would be : MdCd0
b = a.join(("M", "C", "0"))
print(b)
# It goes inbetween the tuple MC0

#F STRINGS
first_name = "Jane"
last_name = "Smith"

sentence = f"My name is {first_name.upper()} {last_name.upper()}"
#Add an f before the string to make it an f string
print(sentence)

#person = {"name": "Jenn", "age":  23}
#sentence = f"My name is {person['name']} and I am {person['age']} years old"
#print(sentence)

#calculation = f"4 times 11 is equal to {4 * 11}"
#print(calculation)
for n in range(1,11):
    sentence = f'The value is {n:02}'#We are "Zero Paddng" by adding a colon the 02
    print(sentence)
#the 2 represents being padded by 2 so the output would be - The value is 01- instead of just 1
#we can format it further by just adding a colon after the n.

from datetime import datetime
birthday = datetime(1990, 1, 1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)

#RANDOM MODULE FUNCTIONS

#random() returns a random number between 0 and 1
import random as rd # putting rd means it is easier to use in the code later on - creating an alias
print(rd.random())

#randint() returns a random number within a given range
import random as rdm
print(rdm.randint(1,5))#input the range in the brackets

#choice() returns a random element from the given sequence
import random as rand
myList = ["anne", "john", "mabel", "joy"]# the example sequence is  list
print(myList)
print(rand.choice(myList))

#randrange() return a random number between a given range
import random as rnd
print(rnd.randrange(5,10))#between the ranges 5 to 10 - 5 6 7 8 9 
print(rnd.randrange(5,10,2))#the 2 is a step so it can only output 5 or 7 or 9
