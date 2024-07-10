# Write a Python program to convert miles into kilometres. Do the following:
# Take the input from the user in miles. Create a function named “showMiles()”.
# Pass the data in miles to this function. Perform the calculations and print the result in kilometres.

miles = float(input("Enter distance in miles"))

def convert_to_km(miles):
    print("Distance in KM are: ", (miles * 1.609))

convert_to_km(miles)