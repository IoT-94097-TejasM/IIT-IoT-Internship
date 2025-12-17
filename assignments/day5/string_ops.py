def str(s):
    count=0
    for i in range(len(s)-1, -1, -1):
        print(s[i], end="") 

    for char in s:
        if char.lower() in 'aeiouAEIOU':
            count=count+1

    print("\nNumber of vowels:", count)