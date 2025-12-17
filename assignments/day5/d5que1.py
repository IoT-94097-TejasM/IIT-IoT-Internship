import math
import os

print("Square root:", math.sqrt(36))
print("Factorial:", math.factorial(5))
print("Ceil:", math.ceil(4.2))
print("Value of pi:", math.pi)



print("Current directory:", os.getcwd())

if not os.path.exists("test"):
    os.mkdir("test")
    print("Folder created")