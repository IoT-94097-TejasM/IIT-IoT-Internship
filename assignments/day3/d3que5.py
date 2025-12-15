def add(a, b=0):        
    return a + b

def subtract(a, b=0):   
    return a - b

def multiply(a, b=1):   
    return a * b

def divide(a, b=1):     
    if b == 0:
        return "Error! Division by zero"
    return a / b



def calculate(operation, x, y):
    return operation(x, y)



while True:
    print("\n--- Function Concepts Demo Menu ---")
    print("1. Addition (Default Parameter)")
    print("2. Subtraction (Keyword Arguments)")
    print("3. Multiplication (Function as Argument)")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program terminated.")
        break

    if choice in [1, 2, 3, 4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            
            print("Result =", add(a)) if b == 0 else print("Result =", add(a, b))

        elif choice == 2:
            
            print("Result =", subtract(a=a, b=b))

        elif choice == 3:
            
            print("Result =", calculate(multiply, a, b))

        elif choice == 4:
            print("Result =", divide(a, b))
    else:
        print("Invalid choice! Try again.")