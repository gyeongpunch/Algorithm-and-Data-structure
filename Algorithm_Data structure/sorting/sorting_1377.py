import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    data.append((int(input()), i))

sorting_data = sorted(data)
max1 = 0

for i in range(n):
    if sorting_data[i][1] - i > max1:
        max1 = sorting_data[i][1] - i
print(max1 + 1)
