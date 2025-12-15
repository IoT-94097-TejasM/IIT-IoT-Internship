text = input("Enter a string: ")

while True:
    print("\n--- String Slicing Menu ---")
    print("1. First N characters")
    print("2. Last N characters")
    print("3. Reverse string")
    print("4. Slice with step")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter N: "))
        print(text[:n])

    elif choice == 2:
        n = int(input("Enter N: "))
        print(text[-n:])

    elif choice == 3:
        print(text[::-1])

    elif choice == 4:
        step = int(input("Enter step value: "))
        print(text[::step])

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")