def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


terms = int(input("Enter number of terms: "))
fibonacci(terms)