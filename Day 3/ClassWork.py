#---------------------------Session1-----------------------------------------
##pre defined functions
# print( )
# input( )
# range( )

##user defined functions
# def function_name():
#     print("user defined function is executed")
# function_name()

##task
# def say_hello():
#     print("Hello programmers")
# say_hello()
# say_hello()

##Task
# number = input("Enter the number to check: ")
# increment=1
# count = 0

   
# if(int(number)):
#     prime_check(number)
#     if(count == 2):
#         print("Number is prime")
#     else:
#         print("Number is not a prime")
# else:
#     print("Enter a valid number")

# def prime_check(number):
#     if(number % increment == 0):
#         count += 1
#     increment += 1
#     if(increment <= number):
#         prime_check(number)

#Loops

#for loop
# fruits = ['a','b','c']
# for fruit in fruits:
#     print(fruit)


#while
# count = 1
# while count <= 5
#     print(count)
# count += 1

#loop controls break  and continue
#break
# for number in range(10):
#     if number == 5 :
#         break
#     print(number)

#continue
# for number in range(10):
#     if number % 2 == 0 :
#         continue
#     print(number)

#Pass
# for number in range(10):
#     if number % 2 == 0 :
#         pass
#     else:
#         print("Odd Number:",  number)


#---------------------------Session2-----------------------------------------


##Tasks
# #print numbers from 1 to 5 using a for loop
# for num in range(1,6):
#     print(num)

# #calculate sum of all even numbers from 1 to 10
# sum_of_even = 0
# for num in range(1,11):
#    if num % 2 == 0 :
#     sum_of_even += num
# print(sum_of_even)

#print square of numbers from 1 to 4 using for loop
# for num in range(1,5):
#     print("Square of ", num, "is ", num**2)


# #calculate the product of number sfrom 1 to 5 usinhg while loop
# num = 1
# product = 1
# while num <= 5:
#     product = product * num
#     num += 1
# print(product)

#functions
# def greet(name):
#     print("Hello, " + name + ". have a good day")
# greet("Ganesh")

# # Turtle python library
# import turtle

# s = turtle.Screen()
# t = turtle.Turtle()

# for i in range(4):
#     t.forward(100)
#     t.left(90)
# turtle.done()

# Turtle python library
# import turtle
# import random

# s = turtle.Screen()
# t = turtle.Turtle()

# for i in range(1000):
#     t.forward(random.randint(1, 30))
#     t.left(random.randint(1, 30))
# turtle.done()

#scope of a variable

#global
# verbose = True
# def example():
#     if verbose:
#         print("Global Verbose variable is accessed in local defination")
# example()

#local
# verbose = True
# def example():
#     verbose = False
#     if verbose:
#         print("Global Verbose variable is accessed in local defination")
#     else:
#         print("Verbose value of false is only inside the function")
#         print(verbose)

# example()
# print(verbose)

# #how to modify global variable locally
# phrase = "Random Phrase"

# def change_it():
#     global phrase
#     phrase=""
#     if(phrase):
#         print("Word still exists",phrase)
#     else:
#         print("Oh no some one over rode")

# print("Before:", phrase )
# change_it()
# print("After:", phrase )


#recursive functions
# def countdown(n):
#     if n <= 0:
#         print('Stop!')
#     else:
#         print(n)
#         countdown(n-1)

# countdown(3)

#recersio - fibonacci series
# def fibonacci_series(n):
#     if n < 0:
#         print("Enter valid number")
    
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_series(n-1) + fibonacci_series(n-2)

# print(fibonacci_series(5))