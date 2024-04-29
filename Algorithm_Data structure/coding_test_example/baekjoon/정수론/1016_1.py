import sys
input = sys.stdin.readline

Min, Max = map(int, input().split())

data = [False] * (Max - Min + 1)

for i in range(2, int(Max ** 0.5) + 1):
    pow = i * i
    start_index = int(Min / pow)
    if Min % pow != 0:
        start_index += 1
    for j in range(start_index, int(Max / pow) + 1):
        data[int((j * pow) - Min)] = True

cnt = 0

for i in range(Max - Min + 1):
    if not data[i]:
        cnt += 1
print(cnt)