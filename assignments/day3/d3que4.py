# Arithmetic operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b


# Menu driven program
while True:
    print("\n--- Arithmetic Operations Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting program...")
        break

    if choice in [1, 2, 3, 4]:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(x, y))

        elif choice == 2:
            print("Result =", subtract(x, y))

        elif choice == 3:
            print("Result =", multiply(x, y))

        elif choice == 4:
            print("Result =", divide(x, y))
    else:
        print("Invalid choice! Please try again.")