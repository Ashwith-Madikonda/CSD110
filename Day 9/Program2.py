# Write a Python program to declare and initialize a tuple with a name “myTuple”.
# Then, take the element from the user and check whether an element exists within a tuple or not.
# If yes, print the element and its position; otherwise, display an error message saying, “Element does not exist.”

myTuple = (1001,1123,1259,"Alice Smith","Finance")
checkItem = input("Enter the item to check: ")

elemnt_found = False
for i,item in enumerate(myTuple):
    if(str(item) == str(checkItem)):
        print("Element ",item," found  at position", i+1)
        elemnt_found = True
    if(i == (len(myTuple) -1) and elemnt_found == False):
        print("Element does not Exit")
