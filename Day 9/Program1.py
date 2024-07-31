# Write a Python program to:
# •    Add an item in a tuple.
# •    Get the 4th element from the last of a tuple.
# •    Remove the last element from the tuple.
# •    Print the final elements of a tuple one by one.



tupleData = (1001,1123,1259,"Alice Smith","Finance")
tuple_add = tupleData + (1110,) #adding elemnt to tuple
print(tuple_add[len(tuple_add)-4])#printing 4th element 
 
tuple_add = tuple_add[:len(tuple_add)-1]#removing last element in tuple

for element in tuple_add:
    print(element)#printing element by element