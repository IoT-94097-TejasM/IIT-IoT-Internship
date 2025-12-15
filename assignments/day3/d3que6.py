# -------- Arithmetic operation functions --------
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


# -------- Calculate function --------
def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


# -------- Testing calculate() with different inputs --------
print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subtract))
print("Multiplication:", calculate(10, 5, multiply))
print("Division:", calculate(10, 5, divide))

print("\nTesting with different values:")
print("Addition:", calculate(7, 3, add))
print("Multiplication:", calculate(6, 4, multiply))
print("Division:", calculate(8, 0, divide))