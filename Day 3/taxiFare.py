# Write a function to calculate taxi fare. Get distance from the user.
# Every km costs $1.5. Calculate the final price with 18% HST. 
# Return the final price back to the function call and print the result.

distance = float(input("Enter distance in km: "))

def taxifare(distance):
    price  = distance * 1.5 * 1.18
    return price

price = taxifare(distance)
print("Fare is  $", price)
