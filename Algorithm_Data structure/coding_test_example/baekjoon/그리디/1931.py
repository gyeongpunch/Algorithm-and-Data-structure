import sys
input = sys.stdin.readline

N = int(input())

data = []
for i in range(N):
    start, end = map(int, input().split())
    data.append((start, end))

data.sort(key = lambda x : (x[1], x[0]))
# print(data)

now_end = -1
# print(end)
cnt = 0
for i in data:
    if now_end <= i[0]:
        # print(i)
        cnt += 1
        now_end = i[1]
print(cnt)