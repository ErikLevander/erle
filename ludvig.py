savings = 100
growth_multiplier = 1.1

print("Enter number of years you want to save")
numberOfYears = int(input())
i = 1
while i < numberOfYears:
  yearY = savings*growth_multiplier
  savings = yearY
  i += 1

totalSum = yearY

print("Din totala summa blir: "); print(totalSum)