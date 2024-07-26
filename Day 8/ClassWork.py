# # Tuple - immutable

# #defining tuple
# tupleExample = (1001,"Alice Smith","Finance") #tuple can have differnet dat types

# #accessing tuple element
# print(tupleExample[0])

# #tupleExample[1] = "changed" #error

# employees = [(1001,"Alice Smith","Finance"),(1002,"John","IT"),(1003,"carol","HR")]

# for employee in employees:
#     print(employee)

# employees[0]= (1001,"Alice S","Finance")
# for employee in employees:
#     print(f"ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}")


# #Exercise 1
# list = [1,2,3,4,5]
# list.append(6)
# list.pop(1)
# list[len(list) - 1] = 10
# print(list)


# #exercise 2
# tuple = (1,2,3,4,5)
# print("third element is : ",tuple[2])

# #hast table
# dictionary_example = {
#     "name": "Alice",
#     "age": 30,
#     "email": "test@email.com"
# }

# print(f" Name: {dictionary_example['name']}")

# #modifying the dictionary
# dictionary_example['location'] = 'Toronto'

# #iteration in dictionary
# for key,value in dictionary_example.items():
#     print(f"{key}:{value}")


#Set

#creating sets
set1 = {1,2,3}
set2 = {3,4,5}

#print(set1[0])#error - as set is unordered and cannot be acced by index

# #union
# union_set = set1 | set2
# print(union_set)

# #intersection
# intersection_set = set1 & set2
# print(intersection_set)

# #difference
# difference_set = set2 - set1
# print(difference_set)

# #symmetric differnce
# symmetric_difference_set = set1 ^ set2
# print(symmetric_difference_set)



#--------------------------------------------------------------------------------------------------#
