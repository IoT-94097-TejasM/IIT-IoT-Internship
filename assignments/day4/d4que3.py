def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()


result = overlapping(list1, list2)


if result:
    print("Lists have at least one common element.")
else:
    print("Lists have no common elements.")