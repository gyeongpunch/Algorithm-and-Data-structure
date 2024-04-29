import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
Time = [0] * (N + 1)
D = [0] * ( N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    Time[i] = data[0]
    for j in data[1:]:
        if j != -1:
            A[j].append(i)
            D[i] += 1
# print(A)
# print(D)
# print(Time)

queue = deque()

for i in range(1, N + 1):
    if D[i] == 0:
        queue.append(i)

result = [0] * (N + 1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        D[next] -= 1
        result[next] = max(result[next], result[now] + Time[now])
        
        if D[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + Time[i])
