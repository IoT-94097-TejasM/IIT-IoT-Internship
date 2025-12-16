def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(feet):
    return feet * 12

def inches_to_cm(inches):
    return inches * 2.54

def feet_to_cm(feet):
    return feet * 30






def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    print(f"{conversion_type}: {result}")



distance = float(input("Enter distance value: "))

print("\n--- Distance Conversions ---")
distance_converter(distance, "Kilometers to Meters", km_to_m)
distance_converter(distance, "Meters to Centimeters", m_to_cm)
distance_converter(distance, "Centimeters to Millimeters", cm_to_mm)
distance_converter(distance, "Feet to Inches", feet_to_inches)
distance_converter(distance, "Inches to Centimeters", inches_to_cm)
distance_converter(distance, "feet to Centimeters", feet_to_cm)