import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, M, K = map(int, input().split())

A = [[] for _ in range(N + 1)]
D = [[sys.maxsize] * K for _ in range(N + 1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    A[start].append((end, weight))

queue = PriorityQueue()
queue.put((0, 1))
D[1][0] = 0

while queue.qsize() > 0:
    now_weight, now_node = queue.get()
    for next_node, next_weight in A[now_node]:
        sum_weight = next_weight + now_weight
        if D[next_node][K - 1] > sum_weight:
            D[next_node][K - 1] = sum_weight
            D[next_node].sort()
            queue.put((sum_weight, next_node))

# print(D)
for i in range(1, N + 1):
    if D[i][K - 1] == sys.maxsize:
        print(-1)
    else:
        print(D[i][K - 1])