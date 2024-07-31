# #--------------------------------------------------------------------------------------
# #dictionaries
# college = {"Name":"triOS", "Program":"Cybersecurity","Year":2024,"Course":"CSD105"}
# print(college)
# print(college["Name"])
# print(college["Program"])
# print(college['Year'])

# x = college.get('Name')
# print(x)
# print(college.get('Course'))


# college['Location'] = 'Toronto'
# college.update({"Course":"CSD110"}) #dictionary update

# print(college)
# print(len(college)) #length function

# #dictionary iteration
# for i in college:
#     print(i) #prints key
#     print(college[i]) #prints values


# # or to print keys or vlues we can use different syntax as well

# for x in college.keys():
#     print(x)

# for x in college.values():
#     print(x)

# for x,y in college.items():
#     print(x,y,sep=":")

# # for country,capital in dict.items: #error
# #     print(country,":",capital)

# #removing item from dictionary
# college.pop("Year")
# college.popitem()
# del college["Course"]
# del college #to delte entire dictionary

# #sort dictionaries by key or values
# myDict = {'rav':10, 'raj':9, 'san':15, 'yas':2, 'sur':32}

# myKeys = list(myDict.keys())
# myKeys.sort()
# sorted_dict = {i:myDict[i] for i in myKeys}
# print(sorted_dict)


# #Execrice 1
# users={}
# while(len(users) < 5):
#     name = input("Enter name of the user: ")
#     languages = []
#     language=""
#     while(language != "0"):
#         language = input("Enter the know language or 0 to exit: ")
#         if(language != 0):
#             languages.append(language)
#     users.update({name:languages})

# languagesKnown = 0
# nameOfUser = "" 
# for name,langues in users.items():
#     if(len(langues) > languagesKnown):
#         languagesKnown = len(langues)
#         nameOfUser = name

# print(nameOfUser, "knows ", languagesKnown, "languages")
# print(users)





# # Initialize an empty dictionary to store user data
# user_data = {}
 
# # Prompt user for inputs
# for i in range(5):
#     name = input("Enter your name: ")
#     languages = input("Enter the languages you are conversationally fluent in (comma separated): ")
#     # Split languages by comma and count the number of languages
#     language_list = languages.split(',')
#     num_languages = len(language_list)
#     # Store the data in the dictionary
#     user_data[name] = num_languages
 
# # Find the maximum number of languages
# max_languages = max(user_data.values())
 
# # Find the users with the maximum number of languages
# max_fluent_users = [name for name, num_languages in user_data.items() if num_languages == max_languages]
 
# # Display the names of the users
# print("Users fluent in the maximum number of languages:")
# for name in max_fluent_users:
#     print(name)


#exercise 2
# name = input("Enter the name of the scholar: ")
# Id = input("Enter the ID of the scholar: ")
# score_list = []
# scores = ("Enter the scores seperated by commas: ")
# score_list = scores.split(',')
# # for x in scores
# scholar = {}
# scholar.update({"Name":name,"ID":Id, "Scores":score_list})
# print(scholar)



#---------------------PANDAS---------------------------------#
# import pandas as pd
# #data
# data = {
#     "Fruit": ["Apple", "Banana", "Cherry"],
#     "Price": [3,2,4]
# }
# df = pd.DataFrame(data)
# print(df)

# #exercise 1: creating data framework
# import pandas as pd
# data = {
#     "Product": ["computer", "Tablet", "Monitor", "printer"],
#     "Sales": [14,33,27,15]
# }
# df = pd.DataFrame(data)

# print(df)
# print(df["Sales"])


#exercise 1:
import pandas as pd
data = {
    "Names": ["Alice", "Bob", "Charlie", "David"],
    "Ages": [24,27,22,32],
    "Cities": ["New York", "Los Angeles", "Chicago", "Miami"],
}
df = pd.DataFrame(data)
print(df)
#exercise 2:
# print(df[["Names","Ages"]])

#exercise 3:
# print(df[df["Ages"] > 25])



