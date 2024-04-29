import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = k
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)
    if cnt < k:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)