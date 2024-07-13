# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# As we did not cover exception handling yet, 
# input validation is not performed in the source code.

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100


num_of_pennies = 0
num_of_nickels = 0
num_of_dimes = 0
num_of_quarters = 0

def inputCount():
    global num_of_pennies, num_of_nickels, num_of_dimes, num_of_quarters, num_of_pennies_in_dollars
    num_of_pennies = int(input("Enter Number of pennies : "))
    num_of_nickels = int(input("Enter Number of nickels : "))
    num_of_dimes = int(input("Enter Number of dimes : "))
    num_of_quarters = int(input("Enter Number of quarters : "))


def totalDollars(num_of_pennies,num_of_nickels,num_of_dimes,num_of_quarters):
    global PENNY_VALUE, NICKEL_VALUE, DIME_VALUE, QUARTER_VALUE, PENNIES_IN_DOLLAR
    if((num_of_pennies < 0) or (num_of_nickels < 0) or (num_of_dimes < 0) or 
       (num_of_quarters < 0)):
        print("Enter valid count")
    else:
        count = ((num_of_pennies * PENNY_VALUE) + (num_of_nickels * NICKEL_VALUE) + (num_of_dimes * DIME_VALUE) + (num_of_quarters * QUARTER_VALUE))
    totalDollars = float(count/PENNIES_IN_DOLLAR)
    if(totalDollars > 1):
        print("Sorry, the amount you entered was more than one dollar.")
    if(totalDollars < 1):
        print("Sorry, the amount you entered was less than one dollar.")
    if(totalDollars == 1):
        print("Congratulations! The amount you entered was exactly one dollar! You win the game!")
        


inputCount()
totalDollars(num_of_pennies,num_of_nickels,num_of_dimes,num_of_quarters)








