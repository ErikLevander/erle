import math
# coding=utf-8

# print: investerat belopp
print('Hur mycket vill du investera?')
investment = float(input())
# print(investment)

# input för att ta årsavkastning som  input från user
print('Hur många procent är årsavkastning?')
annualReturn = int(input())/100
print(annualReturn)

# print: antal år
print('Hur många år vill du spara?')
years = int(input())
# print(years)

# investerat belopp x (1+årsavksatning)^antal år
finalReturn = investment * (1 + annualReturn) ** years
theFinalReturn = math.trunc(finalReturn)
monthlyReturn = theFinalReturn / 12
theFinalMonthlyReturn = math.trunc(monthlyReturn / 12)

print('Din besparing kommer efter ' + str(years) + ' år vara ' + str(theFinalReturn) + 'kr' + ' Såhär mycket får du varje månad på dina besparing ' + str(theFinalMonthlyReturn))