import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = 0

for i in data:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = (start + end) // 2 # 27, 17, 12, 14, 15
    sum = 0
    cnt = 0
    # print(mid, '!!!')
    for i in data:
        if sum + i > mid: # 1 2 3 4 5 | 6 7 | 8 | 9 |
            # print(i, '@@@')
            cnt += 1
            sum = 0
        sum += i
    if sum != 0:
        cnt += 1
    # print(cnt, '@@@@')
    if cnt <= M:
        end = mid - 1 # end = 26, end = 16
    else:
        start = mid + 1 # start = 13, start = 15, start = 16, start = 17
    # print(start, end, '!!!!')
print(start)