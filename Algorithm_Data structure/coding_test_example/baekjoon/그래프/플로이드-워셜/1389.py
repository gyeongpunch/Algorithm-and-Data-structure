import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = [[sys.maxsize for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    D[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    D[a][b] = 1
    D[b][a] = 1


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

# print(*D, sep = '\n')
result = [0] * (N + 1)
for i in range(1, N + 1):
    result[i] = sum(D[i][1:])

# print(result)
min_value = min(result[1:])

for i in range(1, N + 1):
    if result[i] == min_value:
        print(i)
        break