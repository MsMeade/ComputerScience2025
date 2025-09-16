# Program to calculate a running total

# Initialise the variable
runningTotal = 0

# Perform the calculations
price1 = float(input("Enter the price of your first item: "))
runningTotal = runningTotal + price1
price2 = float(input("Enter the price of your second item: "))
runningTotal = runningTotal + price2
price3 = float(input("Enter the price of your third item: "))
runningTotal = runningTotal + price3

# Display the output
print("Total amount is", round(runningTotal,2))