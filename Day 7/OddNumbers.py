# Write a Python program to declare and initialize a list with a name “myList.” 
# Write a code to find odd numbers in a list. Display all the odd numbers one by one.

myList = [1,2,3,5,6,8,10,12,13,15,16,18]

for i in myList:
    if(i % 2 != 0):
        print(i)