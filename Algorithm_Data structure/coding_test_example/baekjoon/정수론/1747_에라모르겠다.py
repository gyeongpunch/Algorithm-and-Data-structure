import sys
input = sys.stdin.readline

N = int(input())
data = [0] * (101)

for i in range(2, 101):
    data[i] = i

for i in range(2, int(101 ** 0.5) + 1):
    if data[i] != 0:
        for j in range(i * 2, 101, i):
            data[j] = 0
print(data)
while True:
    if data[N] != 0:
        str_N = str(N)
        if str_N == str_N[::-1]:
            print(N)
            break
        else:
            N += 1