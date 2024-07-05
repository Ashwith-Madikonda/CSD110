#Write a Python program to take the input (1-7) from the user.
# Based on the user input, print the days of the week (for example: Monday, Tuesday, and so forth). 
#Secondly, if the day is between Monday to Friday, then print, “It is a weekday”; otherwise print, “It is a weekend.”
#Note: If the user enters a negative value or value greater than 7, then you need to display an error message.

DayNumber= int(input("Enter day number: "))
if(DayNumber < 1 or DayNumber > 7):
    print("Enter valid Day number")
elif(DayNumber == 1):
    print("Monday")
elif(DayNumber == 2):
    print("Tuesday")
elif(DayNumber == 3):
    print("Wednesday")
elif(DayNumber == 4):
    print("Thursday")
elif(DayNumber == 5):
    print("Friday")
elif(DayNumber == 6):
    print("Saturday")
else:
    print("Sunday")

if(DayNumber >= 1 and DayNumber <=5):
    print("It is a weekday")
else:
    print("It is a weekend")


