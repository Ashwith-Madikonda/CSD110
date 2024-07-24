# #List - ordered set of values

# prime = [2,3,5,7,11,13,17,19,23]
# print(prime[2])
# print(prime[-2])

# # Nested List
# list1 = ["Blue",1,['x','y','z'],[1,2,3]]
# print(list1[0])


# #membership operators - "in" & "not in"
# prime = [2,3,5,7,11,13,17,19,23]
# print (3 in prime)
# print (6 in prime)


# #Appending elements to list
# aList = [123, 'XYZ', 'Zara', 'abc']
# aList.append(2009)
# aList.extend(2009,2001)
# aList.insert(3,"2001")

# #Claer function
# a = ['blue','pink']
# a.clear()
# print(a)


# #exercises
# #Class Exercise Code:
# # Get number of employees and their salaries for a department

# def get_department_data(department_name):

#     num_employees = int(input(f"Enter the number of employees in {department_name}: "))

#     salaries = []

#     for i in range(num_employees):

#         salary = float(input(f"Enter salary for employee {i+1} in {department_name}: "))

#         salaries.append(salary)

#     return salaries
 
# # Calculate average salary

# def calculate_average_salary(salaries):

#     return sum(salaries) / len(salaries)
 
# # Find second richest salary

# def find_second_richest(salaries):

#     unique_salaries = []

#     for salary in salaries:

#         if salary not in unique_salaries:

#             unique_salaries.append(salary)

#     unique_salaries.sort(reverse=True)

#     return unique_salaries[1] if len(unique_salaries) > 1 else None
 
# # Find common salaries between two departments

# def find_common_salaries(salaries1, salaries2):

#     common_salaries = []

#     for salary in salaries1:

#         if salary in salaries2 and salary not in common_salaries:

#             common_salaries.append(salary)

#     return common_salaries
 
# # Get data for two departments

# department1 = "Department 1"

# department2 = "Department 2"
 
# salaries_dept1 = get_department_data(department1)

# salaries_dept2 = get_department_data(department2)
 
# # Calculate average salaries

# avg_salary_dept1 = calculate_average_salary(salaries_dept1)

# avg_salary_dept2 = calculate_average_salary(salaries_dept2)
 
# # Find second richest salaries

# second_richest_dept1 = find_second_richest(salaries_dept1)

# second_richest_dept2 = find_second_richest(salaries_dept2)
 
# # Find common salaries

# common_salaries = find_common_salaries(salaries_dept1, salaries_dept2)

# """The .2f in the code is a formatting specification used in Python's formatted string literals (also known as f-strings). It specifies that the number should be formatted as a floating-point number with two decimal places."""

# # Display results

# print(f"\nAverage salary in {department1}: {avg_salary_dept1:.2f}")

# print(f"Average salary in {department2}: {avg_salary_dept2:.2f}")
 
# if second_richest_dept1 is not None:

#     print(f"Second richest salary in {department1}: {second_richest_dept1:.2f}")

# else:

#     print(f"Not enough unique salaries in {department1} to determine the second richest salary.")
 
# if second_richest_dept2 is not None:

#     print(f"Second richest salary in {department2}: {second_richest_dept2:.2f}")

# else:

#     print(f"Not enough unique salaries in {department2} to determine the second richest salary.")
 
# print(f"Common salaries between {department1} and {department2}: {common_salaries}")

 
