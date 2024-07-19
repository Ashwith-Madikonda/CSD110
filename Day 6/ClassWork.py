#Nested Loops

# #Analog clock - using nested loop
# #Considering clock starts 12:00 AM - Midnight
# import time
# import datetime

# considerCurrentTime = True
# while(1):
#     for h in range(0,24):
#         for m in range(0,60):
#             for s in range(0,60):
#                 if(considerCurrentTime):
#                     h = datetime.now()                
#                 time.sleep(1)
#                 print(h,":",m,":",s)
#                 if(s==59):
#                     s=0
#                 if(m==59 and s==59):
#                     m=0
#                 if(h==23 and m==59 and s==59):
#                     h=0
                    
# #for loop variations
# for i in range(2,6):
#      print(i)
# for i in range(15,0,-6):
#      print(i)


#Printing patterns

# #Pattern 1
# for i in range(0,8):
#     print(i * str(i))
            

#Pattern 2
# for i in range(0,7):
#     print(i * "*")
            
# # Pattern 3
# for i in range(0,6):
#     s = ""
#     for j in range(0,i):
#         s= s+str(i+j)
#     print(s)

# Pattern 4
# for i in range(6,1):
#     string = ""
#     for j in range(6,1):
#        string = string + str(j)
#     print(string)


#-------------------------------------------------------------------------------------------------------------

#OOPs

# #class
# class Person: #class
#     def __init__(person, name, age): #1st param is object instance of class Person
#         person.name = name #attributes are name and age
#         person.age = age

# # if __name__ == "__main__" :
# p = Person("Ashwith", 28)
# print(p.name)

#inheritence

# class Person:
#     def __init__(self):
#         pass

# #single level inheritence
# class Employee(Person): #inherites Person
#     def __init__(self):
#         pass

# #Muti level inheritence
# class Manager(Employee): #inherites Employee
#     def __init__(self):
#         pass

# #Mutiple level inheritence
# class Manager(Person,Employee): #inherites Employee and Person
#     def __init__(self):
#         pass



# #Encapsulation 
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def _protected_method_(self):
#         print("Protected method")
    
#     def __private_method__(self):
#         print("Private method")
    
#     def publicMethod(self):
#         print("Public method")


# Polymorphism
# print("Hello", end="\n")
# print("Ashwith")
# print(len([1,2,3,4,5]))

        

#Task

# class Shape:
#     def area(self):
#         pass
# class Rectangle (Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height

# class Circle (Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius

# shapes = [Rectangle(4, 5), Circle(3)]
# print(shapes)

# for shape in shapes:
#     print(shape.area())


# #Exercise 1: Bank Account
# class BankAccount:
#     def __init__(self, account_number, account_holder_name, initial_balance=0):
#         self.__account_number = account_number
#         self.__account_holder_name = account_holder_name
#         self.__account_balance = initial_balance
 
#     def deposit(self, amount):
#         if amount > 0:
#             self.__account_balance += amount
#             return True
#         else:
#             return False
#     def display_account_info(self):
#       print("Account Holder Name:", self.__account_holder_name)
#       print("Account Number:", self.__account_number)  
#       print("Account Balance:", self.__account_balance)
 
# # Create an instance of the BankAccount class
# account = BankAccount("123456789", "John Doe", 1000)
# # Deposit money into the account
# account.deposit(1500)
# # Display account information
# account.display_account_info()


# #Exercise 3: Student
# class Student:
#     def __init__(self, name, age, grade, course):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.course = course
 
#     def enrollToCourse(self,course):
#         self.course = course

#     def studentDetails(self):
#       print("Student Name:", self.name)
#       print("Student Age:", self.age)  
#       print("Student Grade:", self.grade)
#       print("Course Enrolled:", self.course)
 

# student = Student("John Doe", "50", "A","None")
# student.enrollToCourse("Python")
# student.studentDetails()