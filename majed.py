print("ränta kalkyl")
print("Hur mycket ska du spara!")
Savings = int(input())
print("Ange hur många år du vill investera")
Time = int(input())
print("Skriv den ränta du önskar")
Rate = float(input())/100

totalRatio = Savings * (1+ (Rate)) ** Time
print ("Du har angett att du ska spara {} dollar varje år om {} år med {} procents ränta, ditt totala sparande kommer att bli ".format(Savings, Time, Rate) + str(totalRatio))