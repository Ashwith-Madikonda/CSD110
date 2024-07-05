# Write a Python program for the following scenario:
# Suppose a buyer will buy some books from a local bookstore. 
# For a specific number of books, they will get loyalty points, which they can redeem in the future (redeem 50 points for 1 free book).
# Write the code for the following:
# •    Take the input for number of books bought.
# •    If the buyer purchases 5 or fewer books, then they will get 20 points.
# •    If the buyer purchases 6 to 10 books, then they will get 40 points.
# •    Buying more than 10 books will give them 100 points
# Print the total number of books the user bought and the total number of loyalty points as well.

NumberOfBooksBought = int(input("Enter number of books bought: "))
loyaltyPoints = 0
if(NumberOfBooksBought<1):
    print("Enter valid input")
elif(NumberOfBooksBought <= 5 and NumberOfBooksBought >= 1):
    loyaltyPoints = 20
elif(NumberOfBooksBought <= 10 and NumberOfBooksBought >= 6):
    loyaltyPoints = 40
else:
    loyaltyPoints = 100

if(NumberOfBooksBought>0):
    print("Total numnber of books bought are", NumberOfBooksBought, "and total number of loyalty point earned are", loyaltyPoints)


