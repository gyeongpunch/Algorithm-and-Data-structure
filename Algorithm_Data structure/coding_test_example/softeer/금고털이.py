import sys
input = sys.stdin.readline

W, N = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key = lambda x : x[1], reverse = True)

result = 0

for i in A:
    if W >= i[0]:
        W -= i[0]
        result += (i[0] * i[1])
    else:
        result += (W * i[1])
        break
print(result)