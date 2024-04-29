import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, M = map(int, input().split())
start_point = int(input())
A = [[] for _ in range(N + 1)]
D = [sys.maxsize] * (N + 1)
visited = [False] * (N + 1)
queue = PriorityQueue()

for _ in range(M):
    start, end, length = map(int, input().split())
    A[start].append((end, length))

# print(*A, sep = '\n')
# print(D)

queue.put((0, start_point))
D[start_point] = 0

while queue.qsize() > 0:
    now = queue.get()
    now_node = now[1]
    if not visited[now_node]:
        # continue
        visited[now_node] = True
        for next in A[now_node]:
            next_node = next[0]
            value = next[1]
            if D[now_node] + value < D[next_node]:
                D[next_node] = D[now_node] + value
                queue.put((D[next_node], next_node))

for i in range(1, N + 1):
    if visited[i]:
        print(D[i])
    else:
        print('INF')