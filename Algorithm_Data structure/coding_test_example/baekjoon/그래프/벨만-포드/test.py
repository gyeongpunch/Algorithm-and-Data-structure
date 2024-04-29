import sys
input = sys.stdin.readline

N, start_city, end_city, M = map(int, input().split())

edge = []
D = [-sys.maxsize] * N

for _ in range(M):
    start, end, cost = map(int, input().split())
    edge.append((start, end, cost))

money = list(map(int, input().split()))

D[start_city] = money[start_city]

for i in range(N + 101):
    for start, end, cost in edge:
        if D[start] == -sys.maxsize:
            continue
        elif D[start] == sys.maxsize:
            D[end] = sys.maxsize
        elif D[end] < D[start] + money[end] - cost:
            D[end] = D[start] + money[end] - cost
            if i > N - 1:
                D[end] = sys.maxsize
# print(D)

if D[end_city] == -sys.maxsize:
    print('gg')
elif D[end_city] == sys.maxsize:
    print('Gee')
else:
    print(D[end_city])