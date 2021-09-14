# Ränta på ränta ez

# Kapital, tid och ränta
kapital = float(input('Ange kapital '))
tid = float(input('Ange hur länge: '))
ranta = float(input('Ange ranta: '))

# Calcualtion
enkel_ranta = (kapital*tid*ranta)/100
ranta_pa_ranta = kapital * ( (1+ranta/100)**tid - 1)

# Displaying result
print('Enkel ranta : %f' % (enkel_ranta))
print('Ranta på ranta: %f' %(ranta_pa_ranta))

#By hardi
