import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
answer = 0

data.sort()

for i in data:
    answer += i * n
    n -= 1
print(answer)