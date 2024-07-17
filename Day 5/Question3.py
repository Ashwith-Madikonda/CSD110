# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.



# Write a Python program for the following problem.

# Let us assume our user is currently working in Germany and wishes to migrate to another country. Ask the user to enter their annual salary in euros. 
# Prompt the user to enter the country to which they want to migrate. Acceptable inputs are: ‘Canada’, ‘USA’, ‘Cambodia’, and ‘United Kingdom’. 
# Other inputs must be rejected.

# By calling the function “convertSalary()”, convert the user’s salary into the corresponding currency based on the conversion rates given below:

# Compare the converted user’s salary against the average salaries of the respective country given below and print, 
# “You will be <rich/poor> in <Country Name> with a salary of <Converted Amount> <Currency Name>.”

# Conversion Rate from Euros to target country currency:

# 1 EUR0 = 1.50 CAD (Canadian Dollar)
# 1 EUR0 = 1.10 USD (US Dollar)
# 1 EUR0 = 4432 Cambodian Riels
# 1 EUR0 = 0.85 Pound Sterling
# Note:
# Students must use the concept of functions during conversions and all the other calculations.
# The function must return the final output value back to the function call.













#Program

#Taking inputs from user
salaryInEuro = int(input("Enter annual salary in euros: "))
contryToMigrate = input("Enter the country you want to Migrate ( Accepted inputs - 'Canada','USA','Cambodia','United Kingdom')): ")

def convertSalary(salary,country): #function definition - conversion of salary
    if(country == "Canada"):
        return salary * 1.5
    elif(country == "USA"):
        return salary * 1.1
    elif(country == "Cambodia"):
        return salary * 4432
    elif(country == "United Kingdom"):
        return salary * 0.85
    else:
        return -1   #returning -1 for invalid country

salaryInOtherCountry = convertSalary(salaryInEuro,contryToMigrate) # calling function and storing value in variable

if(salaryInOtherCountry != -1):
    if(contryToMigrate == "Canada"): #Checking the country 
        if(salaryInOtherCountry >= 56000):#Checking with average salary 
            print("You will be rich in Canada with with a salary of ",salaryInOtherCountry," CAD" )
        else:
            print("You will be poor in Canada with with a salary of ",salaryInOtherCountry," CAD" )
    elif(contryToMigrate == "USA"):#Checking the country
        if(salaryInOtherCountry >= 45000):#Checking with average salary 
            print("You will be rich in USA with with a salary of ",salaryInOtherCountry," US Dollars" )
        else:
            print("You will be poor in USA with with a salary of ",salaryInOtherCountry," US Dollars" )
    elif(contryToMigrate == "Cambodia"):#Checking the country
        if(salaryInOtherCountry >= 7649856):#Checking with average salary 
            print("You will be rich in Cambodia with with a salary of ",salaryInOtherCountry," Combodian Riel" )
        else:
            print("You will be poor in Cambodia with with a salary of ",salaryInOtherCountry," Combodian Riel" )
    else: #United Kindom is the country
        if(salaryInOtherCountry >= 45423):#Checking with average salary 
            print("You will be rich in United Kingdom with with a salary of ",salaryInOtherCountry," Pound Sterling" )
        else:
            print("You will be poor in United Kingdom with with a salary of ",salaryInOtherCountry," Pound Sterling" )
else: #Invalid country
    print("Enter a valid country")



