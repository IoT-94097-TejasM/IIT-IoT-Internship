# Program to check numeric palindrome

num = input("Enter a 5-digit number: ")

if len(num) != 5 or not num.isdigit():
    print("Please enter a valid 5-digit number.")
else:
    rev = num[::-1]
    if num == rev:
        print("The number is a Palindrome.")
    else:
        print("The number is not a Palindrome.")

