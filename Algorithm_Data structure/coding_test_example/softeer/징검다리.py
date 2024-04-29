import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

result = [1] * N

for i in range(1, N):
    result_max = 0
    for j in range(i):
        if data[i] > data[j]:
            if result_max < result[j]:
                result_max = result [j]
    result[i] = result_max + 1
# print(result)
print(max(result))