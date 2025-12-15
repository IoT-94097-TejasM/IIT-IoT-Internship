# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function to find power
def power(base, exp):
    if exp == 0:          # base case
        return 1
    else:
        return base * power(base, exp - 1)


# Testing the functions
num = 5
print("Factorial of", num, "=", factorial(num))

base = 2
exponent = 4
print(base, "power", exponent, "=", power(base, exponent))