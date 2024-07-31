# Write a Python program for the following:
# •    Take a string from the user and store it in a “myString”.
# •    Convert the string into uppercase.
# •    Find the length of the string.
# •    Reverse the string.
# •    Check whether the string is a palindrome or not. 
# A palindrome is a word spelled the same backwards and forwards: for example, radar, level, and racecar.

myString = input("Enter the input string: ")
print(myString.upper())
lengthOfString = len(myString)
reversed_string = myString[::-1]

if(myString == reversed_string):
    print("Entered string is a pallindrome")
else:
    print("Entered string is not a pallindrome")