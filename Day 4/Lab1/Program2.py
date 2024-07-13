# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# As we did not cover exception handling yet, 
# input validation is not performed in the source code.


num1 = 0
num2 = 0
operator = ''

def takeInput():
    global num1, num2, operator 
    num1= float(input("Enter Number 1: "))
    num2= float(input("Enter Number 2: "))
    operator= input("Enter operator: ")


def displayResult(num1,num2,operator):
    if(((num1 < 1) or (num2 < 1)) and ((operator != '+') or
        (operator != '-') or (operator != '*') 
        or (operator != '/'))):
        print("Enter valid numbers and operator")
    else:
        if(operator == '+'):
            print(num1,operator,num2," = ",(num1+num2))
        if(operator == '-'):
            print(num1,operator,num2," = ",(num1-num2))
        if(operator == '*'):
            print(num1,operator,num2," = ",(num1*num2))
        if(operator == '/'):
            print(num1,operator,num2," = ",(num1/num2))

takeInput()
displayResult(num1,num2,operator)








