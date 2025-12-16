def histogram(numbers):
    for n in numbers:
        print('*' * n)

lst = list(map(int, input("Enter integers separated by space: ").split()))


histogram(lst)