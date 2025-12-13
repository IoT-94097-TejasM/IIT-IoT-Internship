# Function to check prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Main program
n = int(input("Enter a number to check prime: "))

if is_prime(n):
    print(n, "is a Prime number")
else:
    print(n, "is not a Prime number")

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers in the given range:")
for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=" ")