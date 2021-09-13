print(" Welcome to Swedbank? ")
Savings = int(input("State the amount you would like to save yearly "))
Time = int(input("Enter number of years you want to invest, please "))
Rate = int(input(" Type interest rate you wish "))
totalRatio = Savings * (1+ (Rate / 100)) * Time
print ("You have enterered that you are going to save {} dollar each year in {} years with {} procent interest rate, your total saving is going be ".format(Savings, Time, Rate) + str(totalRatio))