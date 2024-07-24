# Write a function that takes 2 lists as parameters. The function must check if both the lists are equal in size. 
# If yes, subtract list 1 from list 2 and return the subtracted list. Otherwise, print a message and return an empty list.

list1 = [1,2,3,4]
list2 = [1,2,7,8,6]

def listCompare(l1,l2):
    if(len(list1) == len(list2)):
        return [list1[i]-list2[i] for i in range(len(list1))]
    else:
        print("Two list are not equal")
        return[]

result = listCompare(list1,list2)
print(result)