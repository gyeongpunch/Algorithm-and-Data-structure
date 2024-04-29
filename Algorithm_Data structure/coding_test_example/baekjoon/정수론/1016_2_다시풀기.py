import sys
input = sys.stdin.readline

Min, Max = map(int, input().split())

def solve(Min, Max):
    data = [1] * (Max - Min + 1)

    for k in range(2, int(Max ** 0.5) + 1):
        s = k * k
        i = 0 if Min % s == 0 else s - (Min % s) # 제곱수의 Min~Max 안에서의 시작 인덱스
        for j in range(i, len(data), s):
            data[j] = 0
    return sum(data)

print(solve(Min, Max))