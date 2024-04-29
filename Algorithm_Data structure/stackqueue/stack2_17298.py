import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
result = [-1] * n
stack = []

for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        result[stack.pop()] = data[i]
    stack.append(i)

for i in result:
    print(i, end = ' ')
