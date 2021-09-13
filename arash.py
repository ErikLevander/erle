print("Hur mycket vill du investera? ")
investment= int(input())
# input for aarsavkastning
print ("Hur många procent är avkastning?")
annualReturn = float(input())
# hur många år vill du spara
print ("hur många år vill du spara?")
years= int(input())
# investment*(1+annualReturn)**year
finalreturn= investment*(1+annualReturn)**years
print ('din besparing efter'+str(years)+'år är'+str(finalreturn)
