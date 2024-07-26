# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Write a Python program for the following scenario by using lists, functions, and loops.

# Instructions:

# Declare and initialize a 9-integer list with the name “myNumbers.”
# During the initialization of this list, store the following numbers in it: 4,6,9,12,17,22,27,33,44.
# By using the concept of loops, iterate through the elements of the list one by one and print them on the console.
# Sort the list as follows:
# a. First, move through the list and find the largest number left in the list.
# b. Swap that number for the last element in the unsorted list.
# c. Reduce the range of the list you are sorting by 1 and repeat steps a and b until there is only 1 element left to consider.
# d. Print the sorted list.







#program
myNumbers = [4,6,9,12,17,22,27,33,44]
print("Sorted List: ", myNumbers)
print("Largest Number: ", max(myNumbers))

#swapping variable - index 1 and 8
myNumbers[1] = myNumbers[1] + myNumbers[8]
myNumbers[8] = myNumbers[1] - myNumbers[8]
myNumbers[1] = myNumbers[1] - myNumbers[8]

#swpping by insertioninsertion
myNumbers.insert(2,33)
myNumbers.pop(3)
myNumbers.insert(-2,9)
myNumbers.pop(-2)



print("After swap and insertion: ", myNumbers)

lenght = len(myNumbers)
for x in range(0,lenght,1):
    if(x == lenght-1):
        print("Final sorted list: ", myNumbers)
        break
    myNumbers.pop() # removing items from list
