#---------------------- Session 1------------------------

conditional statements


#if Statement
a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if (a == b):
    print("a is equal to b")


#if else statement
a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if (a == b):
    print("a is equal to b")
else:
    print("a is not equal to b")

#Task
if else statement
a= int(input("Enter temperature in Farenheit: "))
if (a < 40):
    print("A little cold, isn't it?")
else:
    print("Nice Weather we are having")

#nested decision
var = 100
if var == 200:
    print("1 - got a true expression")
elif var == 100
    print("2 - got a true expression")
else
    print("3 - no true expression")


#task
salary= int(input("Enter your Salary: "))
if (salary < 0):
    print("Enter valid salary")
elif(salary < 30000):
    print("You must earn atleast 30000 to qualify for loan.")
else: 
    experience = int(input("Enter work experience in years"))
    if(experience < 2):
        print("You must have atleast 2 years on current job  to qualify for loan.")
    else:
        print("You are eligible for loan")


#---------------------- Session 2------------------------

#Truthy and Falsy - Boolean expressions
if(1):
    print("True")
else:
    print("False")

#Exercise1 - sum of 3 given numbers
a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
c= int(input("Enter number 3:"))

if(a==b):
    if(a==c):
        print(3*(a+b+c))
    else:
        print(2*(a+b+c))
elif(b==c):
    print(2*(a+b+c))
elif(a==c):
    print(2*(a+b+c))
else:
    print(a+b+c)

#Exercise2 - range
num= int(input("Enter number: "))
if(num < 1):
    print("Enter valid number")
elif(num%2 == 0):
    if(num > 1 and num < 6):
        print("Range B")
    elif(num >= 6 and num < 21):
        print("Range C")
    else:
        print("Range D")
else:
    print("Range A")


#Exercise7 - Grades
grade= int(input("Enter grade: "))
if(grade < 1 or grade > 100):
    print("Enter valid Grade")
elif(grade == 100):
    print("Perfect")
elif(grade <= 99 and grade >= 90):
    print("A")
elif(grade <= 89 and grade >= 80):
    print("B")
elif(grade <= 79 and grade>= 70):
    print("C")
elif(grade <= 69 and grade >= 60):
    print("D")
else:
    print("F")










