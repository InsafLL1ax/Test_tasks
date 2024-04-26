size, direction = input().split()
size = int(size)

matrix = [list(map(int, input().split())) for _ in range(size)]
operations = []

if direction == "R":
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            operations.append((i, j, j, size - i - 1))
            operations.append((j, size - i - 1, size - i - 1, j))
            operations.append((size - i - 1, j, i, size - j - 1))
else:
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            operations.append((j, i, i, size - j - 1))
            operations.append((size - i - 1, size - j - 1, size - j - 1, i))
            operations.append((i, size - j - 1, size - i - 1, j))

print()
print(len(operations))
for op in operations:
    print(*op)