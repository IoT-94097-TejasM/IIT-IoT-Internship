def print_binary(num):
    if num == 0:
        print("Binary:", 0)
        return

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    print("Binary:", binary)

# Example usage
n = int(input("Enter a number: "))
print_binary(n)