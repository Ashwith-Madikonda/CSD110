# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.





# Write a Python program using if-elif-else and nested if-else for the following.

# Note: The user must enter the colour in lowercase letters.

# Declare the following global variables for the three colours with the following values:
# RED = "red"
# BLUE = "blue"
# YELLOW = "yellow"

# This program must prompt the user to input two different primary colours: “colour1” and “colour2.”
# Consider the following situations:

# If color1 is not a primary colour (RED, BLUE, or YELLOW), then print the error message: “Error: Invalid Colour1.”
# If color2 is not a primary colour, then print the error message: “Error: Invalid Colour2.”
# If colour1 and colour2 are the same, then print the error message: “Error: The two colours you entered are the same.”
# Otherwise, if the inputs are valid, the program will report the secondary colour which is the mix of the two primary colours as follows:

# When first colour is “RED”:
# RED+BLUE=PURPLE
# RED+YELLOW=ORANGE

# When first colour is “BLUE”:
# BLUE+RED=PURPLE
# BLUE+YELLOW=GREEN

# When first colour is “YELLOW”:
# YELLOW+RED=ORANGE
# YELLOW+BLUE=GREEN














#Program 

#Declaring global variables
RED = "red"
BLUE = "blue"
YELLOW = "yellow"


#Taking inputs from user
colour1 = input("Enter primary color 1 (primary colors are 'red','blue','yellow', enter in lower case letters only):  ")
colour2 = input("Enter primary color 2 (primary colors are 'red','blue','yellow', enter in lower case letters only):  ")
invalidColors = False
if((colour1 != RED) and (colour1 != BLUE) and (colour1 != YELLOW)): #Validating color 1
    print("Error: Invalid Colour 1.")
    invalidColors = True
if((colour2 != RED) and (colour2 != BLUE) and (colour2 != YELLOW)):#Validating color 2
    print("Error: Invalid Colour 2.")
    invalidColors = True


if(colour1 == colour2): #Validating if two color are same
    print("Error: The two colours you entered are the same.")
    invalidColors = True

if(invalidColors):
    print("Try again with valid colors and combinations") #If any color is invalid or wrong combination is selected
else: #All valid inputs
    if(colour1 == RED): #color 1 is red
        if(colour2 == BLUE): #color 2 is blue
            print(colour1,"+",colour2,"= PURPLE")
        else:#color 2 is yellow
            print(colour1,"+",colour2,"= ORANGE")
    elif(colour1 == BLUE): #color 1 is blue
        if(colour2 == RED):#color 2 is red
            print(colour1,"+",colour2,"= PURPLE")
        else:#color 2 is yellow
            print(colour1,"+",colour2,"= GREEN")
    else: #color 1 is yellow
        if(colour2 == RED):#color 2 is red
            print(colour1,"+",colour2,"= ORANGE")
        else: #color 2 is blue
            print(colour1,"+",colour2,"= GREEN")
