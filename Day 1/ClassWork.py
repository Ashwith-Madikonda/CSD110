#Firts Program in python
print('Hello World!')

# variables
course = "CSD 110, Intoduction to programming using Python"
room_number = 302
average_grade = 2.8

#Printing mutiple items at once
print(course,"\n",room_number,"\n",average_grade)

#Single line comment

"""
Multiline Comment
"""


#Using input Function
age = input("Enter your age:")
print("you are", age, "years old")

#Task
name = input("Enter your name:")
print("Hello", name,"you are",age,"years old")

#Task
num1 = input("Enter Number 1:")
num2 = input("Enter Number 2:")
num3 = num1+num2
print(num3)

#Type Conversion
num1 = input("Enter Number 1:")
num2 = input("Enter Number 2:")
num3 = int(num1)+int(num2)
print(num3)

#Task
distance_in_kms = input("Enter the distance travelled in Kilometers: ")
distance_in_miles = (float(distance_in_kms)/1.60934)
print("Distance driven in miles:", distance_in_miles)




#---------------------- Session 2------------------------


# Operators
print(13%3) #gives reminder
print(13/3)
print(13//3) #float division- rounds up to nearest value
print(10*3)
print(10**3)


#Order of operations - PEMDAS = Parentahesis, Exponetiation, Multiplication, Division, Addition, Substraction
order_a = 12 *4+5
order_b = 12 *(4+5)
print(order_a, order_b)

#Types
a = 10
b = 9.6
c = "Hello World!"
print("Type of variable a is", type(a))
print("Type of variable a is", type(b))
print("Type of variable a is", type(c))

# Data outputs
a = 10
b = 15
c = 20
d = 30

print(a,b,sep=";",end="......")


#Augmented Assignmnet
a = 10
b = 15
a += b
a -= b

# string concatenation
string1 = "Hi"
string2 = "Ashwith"
print(string1+string2)


#stack - LIFO
stack=['Ashwith','Reddy']
stack.append('Madikonda')
print(stack)
stack.pop()
print(stack)

#Queue - FIFO
queue=['Ashwith','Reddy']
queue.append('Madikonda')
print(queue)
queue.pop(0)
print(queue)


# Hash table - is a key:value  pair - referred as dictionaries
dictionary = {
    "Name" : "Ashwith",
    "Age": 100,
    "Sem": 3
}
print(dictionary['Name'])
dictionary['Age'] = 50
print(dictionary['Age'])
dictionary['College'] = 'Sault'
print(dictionary)
del dictionary['College']
print(dictionary)
del dictionary
print(dictionary)


