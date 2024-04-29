import sys
input = sys.stdin.readline
import heapq

N, M, K = map(int, input().split())

A = [[] for _ in range(N + 1)]
D = [[sys.maxsize] * K for _ in range(N + 1)]

for i in range(M):
    start, end, weight = map(int, input().split())
    A[start].append((end, weight))

D[1][0] = 0
pq = [(0, 1)]

while pq:
    now_weight, now_node = heapq.heappop(pq)
    for next_node, next_weight in A[now_node]:
        sum_weight = now_weight + next_weight
        if D[next_node][K - 1] > sum_weight:
            D[next_node][K - 1] = sum_weight
            D[next_node].sort()
            heapq.heappush(pq, [sum_weight, next_node])

print(D)

for i in range(1, N + 1):
    if D[i][K - 1] == sys.maxsize:
        print(-1)
    else:
        print(D[i][K - 1])