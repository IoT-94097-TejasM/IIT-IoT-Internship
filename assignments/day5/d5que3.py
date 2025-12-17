import geometry

r = float(input("Enter radius of circle: "))
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

print("Area of circle:",geometry.area_of_circle(r))
print("Area of rectangle:", geometry.area_of_rectangle(length, breadth))