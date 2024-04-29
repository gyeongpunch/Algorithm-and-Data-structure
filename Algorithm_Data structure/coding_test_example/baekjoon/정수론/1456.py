import sys
input = sys.stdin.readline

A, B = map(int, input().split())

data = [0] * (10000001)

for i in range(2, 10000001):
    data[i] = i

# print(data)
for i in range(2, int(10000001 ** 0.5) + 1):
    if data[i] == 0:
        continue
    for j in range(i * 2, 10000001, i):
        data[j] = 0

cnt = 0
# print(data)
for i in range(2, 10000001):
    if data[i] != 0:
        tmp = data[i]
        while data[i] * tmp <= B:
            if data[i] * tmp >= A:
                cnt += 1
            tmp *= data[i]
print(cnt)