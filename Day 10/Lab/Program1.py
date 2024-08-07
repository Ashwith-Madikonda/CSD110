# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Instructions:

# Write a menu-driven program to add or delete products from a shopping cart. 
# You should use dictionary to store the product and its brand.


# WELCOME TO THE AMANDO SHOPPING SITE

# Add a product to the cart.
# Search for a product.
# Delete a product from the cart.
# Display the contents of the cart.
# Purchase items.
# Quit.
# Take an empty dictionary with the name “shoppingCart.” 
# The dictionary should always store “product-name”, “product-price”, and “brand” as key-value pairs.

# Based on the user’s input in response to the main menu, do the following:

# The user can add a new product to the shopping cart. 
# A maximum of five products can be entered.
#  If the count is exceeded, then display the following message:
#  “Cart is full.”

# Search for a product by its name. If the name is found, then display the results. 
# If not, display the following message: “No product exists with this name.”

# Delete an existing product. 
# If the cart is empty then display the message: “Cart is empty, no item is found.” 
# If the product is not in the cart, display the message: “Product not found in cart.”

# Display the items in the cart.
#  If there are no items in the cart, then display the message: “Cart is empty.”

# Purchasing items should total up the product prices for the products in the cart 
# and display the total along with a message: “Complete purchase (Y/N)?” If the user answers “Y” or “y”
#  then display the message: “Thank you for your business.” and empty the cart. 
# If the user answers “N” or “n” then display the message: “Please continue shopping.” 
# If the user answers anything else, display the message: “Please answer either Y or N.” and repeat this process.

# NOTE: If the user tries to purchase an empty cart, display the message: “Cart is empty, please select an item before completing purchase.”
# On entering the sixth option, user exits from the whole program.




#Program - Source code
shoppingCart = {}

def addProductToCart(product): # addding item to cart method
    shoppingCart[len(shoppingCart)] = product
    print("Product added successfully")
    welcome() #recursive function

def searchForProduct(searchTerm): # searching item in cart method
    results = []
    for x in shoppingCart:
        if(searchTerm in shoppingCart[x]['ProductName']):
            results.append(shoppingCart[x])
    if(len(results)):
        print("Product(s) for your search term are \n",results)
    else:
        print("No products exists with this name")
    welcome() #recursive function

def deleteProduct():# deleting item from cart method
    if(len(shoppingCart)):
        print("Select a product to delete: ")
        for x in shoppingCart:
            print(x+1, " for ", shoppingCart[x])
        deleteOption = int(input())
        if(deleteOption < 1 or deleteOption > (len(shoppingCart))):
            print("Product not found in cart")
        else:
            del shoppingCart[deleteOption-1]
            print("Selected item deleted from the cart")
    else:
        print("Cart is empty, no item is found")
    welcome() #recursive function


def displayCart(): # displaying cart method
    if(len(shoppingCart)):
        print("Contents of cart are ")
        for x in shoppingCart:
                print(shoppingCart[x])
    else:
        print("Cart is empty")
    welcome() #recursive function

def purchaseItems(shoppingCart): # purchasing  cart method
    if(len(shoppingCart)):
        cartTotal = 0
        for x in shoppingCart:
            cartTotal += int(shoppingCart[x]['ProductPrice'])
        print("Total value of cart is ", cartTotal, ". \n Complete purchase (Y/N)?")
        confirmation = input()
        if(confirmation == 'y' or confirmation == 'Y'):
            print("Thank you for your business")
            shoppingCart = {}
        elif(confirmation == 'n' or confirmation == 'N'):
            print("Please continue shopping.")
            welcome() #recursive function
        else:
            print("Please answer either Y or N.")
            purchaseItems()
    else:
        print("Cart is empty, please select an item before completing purchase.")
    welcome()


print("WELCOME TO THE AMANDO SHOPPING SITE:  \n \n") # program execution satrting point

def welcome(): # 
    WelcomeText = '''Please enter what you like to do \n \n
    1. Add a product to the cart. \n
    2. Search for a product. \n
    3. Delete a product from the cart. \n
    4. Display the contents of the cart. \n
    5. Purchase items. \n
    6. Quit. \n
    '''
    print(WelcomeText)
    userChoice = int(input())
    if(userChoice > 0 and userChoice < 6): #user selection conditional statements
        if(userChoice == 1):
            if(len(shoppingCart) == 5):
                print("Cart is Full")
                welcome()
            else:
                productName = input("Please enter product name: \n")
                productPrice = input("Please enter product price: \n")
                productBrand = input("Please enter product brand: \n")
                product = {}
                product.update({"ProductName":productName, "ProductPrice":productPrice, "Brand":productBrand})
                addProductToCart(product)
        if(userChoice == 2):
            searchTerm = input("Please enter product name for searching: \n")
            searchForProduct(searchTerm)
        if(userChoice == 3):
            deleteProduct()
        if(userChoice == 4):
            displayCart()
        if(userChoice == 5):
            purchaseItems(shoppingCart)
    elif(userChoice == 6):
        print("Thank you!") #exit
    elif(userChoice < 1 or userChoice > 5):
        print("You entred a wrong option")
        welcome()

welcome() #intitial function call
