# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Write a Python program for the following scenario using functions and for loop.

# Instructions:

# Let us suppose your doctor asks you to record your daily data intake of calories during a diet.
# Note that every day, the number of calories should be increased by a certain small percentage.

# Ask the user to enter the following:
# Starting daily calorie intake.
# Average daily percentage decrease.
# The number of days.

# The user must enter only positive values, otherwise an error will be printed on the console,
# and the user must be prompted to enter the values again.

# If the values are positive, you must decrease by the percentage for the specified number of days to the start of the diet.
# Note: If the diet decreases calories below 1200 then you must stop decreases and produce a note when the diet stabilized.

# Note: Day 1 count will start from the original starting count.

# Print the calories data on the daily basis.







#program
starting_daily_calorie = 0 #varibles declaration
average_percentage_decrease = 0
days = 0
def inputDietPlan(): #function definition
    global starting_daily_calorie, average_percentage_decrease, days
    starting_daily_calorie = int(input("Enter starting daily calorie intake: ")) #taking daily calorie as input from user
    average_percentage_decrease = int(input("Enter percentage to reduce calories: ")) #taking average daily percentage as input from user
    days = int(input("Enter number of days: ")) #taking numbers of days as input from user
inputDietPlan() #function calling
while(starting_daily_calorie < 1 or average_percentage_decrease < 1 or days < 1): #checking validity of inputs
    print("Invalid Inputs entered, please enter the details again. \n")
    inputDietPlan() #recallinmg function when invalid inputs were given
if(starting_daily_calorie > 1200):
    for i in range(0,days,1):
        print(f"Day {i+1}: {starting_daily_calorie} calories")
        starting_daily_calorie = starting_daily_calorie - ((starting_daily_calorie * average_percentage_decrease)/100)#printing daily calories
        if(starting_daily_calorie < 1200):
            print(f"Diet stabilized at day {i+2} with {starting_daily_calorie} calories (below 1200)")#printing diet stabilization message
            break
        if(i == days-1 and starting_daily_calorie > 1200):
            print(f"Diet not stabilized not stabilized with this plan, please modify your plan") # message if diet is not stabilized in given days
else:
    print("Diet is already stabilized")


