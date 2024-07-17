# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.







# Write a Python program using if-elif-else approach for the following problem.

# Display the following messages and get inputs from the user:

# Enter the month in the numeric form.
# Enter the day in numeric form.
# Enter the year in two numeric digits (for example: 98, 20, 21).
# In case of an invalid user input for day, month, or year, print the following messages:

# Month: “Error: Invalid Month Input”
# Day: “Error: Invalid Day Input”
# Year: “Error: Invalid Year Input”


# Check that you have been given an appropriate day input for a particular month. 
# For example, the 48th of a month or the 30th of February are not valid. For simplicity’s sake, 
# you can assume that any 4th year has a 29th of February rather than do the full calculation. 
# If the day is not appropriate, print the following message: “Error: There is no such date in the calendar.”

# For all valid inputs from the user, print the date with all three inputs in a date format along with the following message:

# “Success: Congratulations! You entered a correct date.”


















#Program 

#Taking inputs from user
month = int(input("Enter the month in the numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = int(input("Enter the year in two numeric digits (for example: 98, 20, 21):"))


if(month > 1 and month < 13): #validating the month
    if(year > 0 and year < 99): #validating the year
        leapYear = 0
        if(year % 4 == 0):
            leapYear = 1 #check for leap year
        
        if( month == 9 or month == 4 or month == 6 or month == 11 ): #checking for months with 30 days
            if(day > 0 and day < 31):
                print("Success: Congratulations! You entered a correct date. \n",day,"/",month,"/",year) #Printing on success
            else:
                print("Error: There is no such date in the calendar.")
        elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or  month == 12 ): #checking for months with 31 days
            if(day > 0 and day < 32):
                print("Success: Congratulations! You entered a correct date. \n",day,"/",month,"/",year) #Printing on success
            else:
                print("Error: There is no such date in the calendar.")
        else:
            if(((day > 0 and day < 30) and (leapYear == 1)) or ((day > 0 and day < 29) and (leapYear == 0))): #checking for february month
                print("Success: Congratulations! You entered a correct date. \n",month,"/",day,"/",year) #Printing on success
            else:
                print("Error: There is no such date in the calendar.") #Printing the error in date
    else:
        print("Year: “Error: Invalid Year Input”") #Printing the error in year
else:
    print("Month: “Error: Invalid Month Input” ") #Printing the error in month