data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

result = []

for col in range(len(data[0])):
    total = 0
    for row in range(len(data)):
        total += data[row][col]
    avg = total / len(data)
    result.append(avg)

print(result)