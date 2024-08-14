# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Write a Python script for the following scenario:

# Develop a Phone Directory Management System Python program using dictionaries.
# Create a dictionary with name "phoneDirectory."
# The dictionary should be empty at the initial stages.
# Display a menu as demonstrated below with multiple choices, 
# so that the user can select one for performing various actions.
# After completing the relevant actions (except for Quit), the menu is displayed again.

# Sample menu:

# WELCOME TO THE GRANN'S PHONE DIRECTORY

# Add a record
# Search a record
# Update a record
# Sort the record alphabetically
# Delete a record
# Display the records  # enhacement in the code for checking the updated records after any action
# Quit
# Enter your choice:

# The dictionary should always store names and phone numbers as a key-value pair.
# Based on the user's input in response to the main menu, add a new name and phone number,
# search a person's phone number, change an existing phone number, display the stored records in sorted form,
# or delete an existing name and phone number. On entering the sixth option (Quit), the user will exit from the whole program.




#Program - Source code:

phoneDirectory = {} #empty dictionary declaration
def addRecord(contact): # addding item to cart method
    phoneDirectory[len(phoneDirectory)] = contact
    print("Record added")
    welcome() #recursive function - calling main menu again

def searchForRecord(searchTerm): # searching a record with name
    results = []
    for key,value in phoneDirectory.items():
        if(searchTerm in str(value)):
            results.append(phoneDirectory[key]) 
    if(len(results)):
        print("Records for your search are")
        for i in results:
            print(i)
    else:
        print("No records found with this name")
    welcome() #recursive function

def updateRecord(contactName):
    if(len(phoneDirectory)):
        results = []
        for key,value in phoneDirectory.items():
            if(contactName in str(value)):
                results.append(key)
        if(len(results)):
            updatedName = input("Enter  name: \n")
            updatedPhoneNumber = input("Enter 10-digit phone number: \n")
            updateContact = {}
            updateContact.update({updatedName:updatedPhoneNumber})
            phoneDirectory[results[0]] = updateContact
            print("Record updated")
        else:
            print("No records found with this name")
    else:
        print("Phone directory is empty, please add records to update")
    welcome() #recursive function

def sortRecords(): #this code did not work - needs refactoring
    sorted_dict = []
    for i in phoneDirectory:
        sorted_dict.append(phoneDirectory[i])
    print("Sorted records are: \n", sorted_dict)
    welcome() #recursive function


def deleteRecord(contactName):# deleting record
    if(len(phoneDirectory)):
        results = []
        for key,value in phoneDirectory.items():
            if(contactName in str(value)):
                results.append(key)
        if(len(results)):
            del phoneDirectory[results[0]]
            print("Record deleted")
        else:
            print("No records found with this name")
    else:
        print("Phone directory is empty, please add records to update")
    welcome() #recursive function


def displayDirectory(): #displaying phone directory
    if(len(phoneDirectory)):
        print("Contacts in the directory are: \n ")
        for x in phoneDirectory:
                print(phoneDirectory[x])
    else:
        print("Phone directory is empty. \n")
    welcome() #recursive function



print("WELCOME TO THE GRANN'S PHONE DIRECTORY:  \n \n") # program execution satrting point

def welcome(): # function definition
    phoneMenu = '''Please enter what you like to do \n \n
    1. Add a record \n
    2. Search a record. \n
    3. Update a record. \n
    4. Sort the record alphabetically. \n
    5. Delete a record. \n
    6. Diplay the phone directory. \n 
    7. Quit. \n
    
    Enter your choice: 
    '''  #multiline string variable

    # option 6 (Dsiplaying the phone directory) is added as anenhacement in the code for checking the updated records after any action.

    print(phoneMenu) #printing the initial menu
    userChoice = int(input()) #taking input from user for performing the task
    if(userChoice > 0 and userChoice < 7): #conditional statements - using if-else
        if(userChoice == 1): #nested conditional statements
            name = input("Enter  name: \n")
            phoneNumber = input("Enter 10-digit phone number: \n")
            contact = {}
            contact.update({name:phoneNumber})
            addRecord(contact) #calling add record function
        if(userChoice == 2):
            searchForRecord(input("Enter name to search: \n"))
        if(userChoice == 3):
            updateRecord(input("Enter the name of the record: \n"))
        if(userChoice == 4):
            sortRecords()
        if(userChoice == 5):
            deleteRecord(input("Enter the name to delete: \n"))
        if(userChoice == 6):
            displayDirectory()
    elif(userChoice == 7):
        print("Thank you, you have exited from the directory") #exit
    elif(userChoice < 1 or userChoice > 7):
        print("You entred a wrong option") #informing user
        welcome()
welcome() #intitial function call
