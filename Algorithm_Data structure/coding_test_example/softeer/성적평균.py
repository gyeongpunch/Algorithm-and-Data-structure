import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

for i in range(K):
    start, end = map(int, input().split())
    # print(sum(data[start - 1 : end]))
    result = sum(data[start - 1 : end]) / (end - start + 1)
    print(format(result, ".2f"))