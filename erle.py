savings = int(input( "Ange sparande: "))
year = int(input( "Hur många år vill du spara? "))
interrest = float(input("Ange räntan i %: "))
# Ändrar % till decimal
interrest = interrest / 100
total_savings = savings * ((1 + interrest) ** year)
# Rundar av till närmaste heltal
total_savings = round(total_savings)
print("Du har på " + str(year) + "år tjänat " + str(total_savings - savings) + "kr")