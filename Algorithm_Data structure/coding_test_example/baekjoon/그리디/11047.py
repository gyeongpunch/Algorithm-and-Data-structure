import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [0] * N
for i in range(N):
    data[i] = int(input())

result = 0

for i in range(N - 1, -1, -1):
    result += K // data[i]
    K %= data[i]
print(result)