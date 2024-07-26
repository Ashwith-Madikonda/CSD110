# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.




# Create a Python program to calculate the average daily high temperature 
# and the average monthly high temperature.

# Instructions:

# Ask the user to enter the number of years.
# Prompt the user to input the average high temperature for each month.
# You must use while loops here.
# After receiving the monthly inputs per year, you must calculate the average high temperature for every year,
# along with the average monthly high temperature over the full period.





#Program - Source code

years = int(input("Enter Number of Years to calculate: ")) #taking years as input from user
monthly_averages = [] #list to store monthly average temperatures
if(years > 0): #checking the validity of years input
    loopVariable = years
    while(loopVariable): # for looping the years entered
        print(f" \n Enter Data for year {loopVariable}:")
        for month in range(0,12,1): #accepting montly average values
            monthly_averages.append(int(input(f"Please enter average high temperature for month {month+1} of year {loopVariable}: ")))
        loopVariable = loopVariable -1
        print(" \n \n")
    yearly_avg=0 #to store average temperatures of a year
    start = 0 #range variable 
    end = 12 #range variable 
    loopVariable = years
    while(loopVariable): #looping over number of yearss
        for i in range(start,end+1,1): #looping to get monthly values
            if(years > 1 and loopVariable == years):
                j=years #llop variable
                months_cumilative = 0
                while(j):
                    month = i #variable for accessing index
                    months_cumilative = months_cumilative + monthly_averages[month]
                    j=j-1
                    month = month + 12
                print(f"Average temperature for month {i+1} is :", months_cumilative/years) #printing monthly averages
            yearly_avg = yearly_avg + monthly_averages[i]
            if(i==end-1):
                print(f"\n Average temperature for Year {loopVariable} is {yearly_avg/12}") #printing yearly average temperature
                start = start+12
                end = end+12
                yearly_avg = 0
                break
        loopVariable = loopVariable - 1
else:
    print("Please enter valid input") #request user to  input valid value

