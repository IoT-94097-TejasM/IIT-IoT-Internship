conversions = [
    lambda t: t * 1000,              
    lambda kg: kg * 1000,            
    lambda g: g * 1000,             
    lambda mg: mg * 0.00000220462    
]


tons = float(input("Enter weight in tons: "))


kg = conversions[0](tons)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print("Kilograms:", kg)
print("Grams:", gm)
print("Milligrams:", mg)
print("Pounds:", lbs)