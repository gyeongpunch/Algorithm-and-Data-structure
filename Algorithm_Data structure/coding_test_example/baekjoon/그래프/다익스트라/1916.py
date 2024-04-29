import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
M = int(input())

A = [[] for _ in range(N + 1)]
D = [sys.maxsize] * (N + 1)
visited = [False] * (N + 1)

for i in range(M):
    start, end, weight = map(int, input().split())
    A[start].append((end, weight))

start_point, end_point = map(int, input().split())
q = PriorityQueue()
q.put((0, start_point))
D[start_point] = 0

while q.qsize() > 0:
    now = q.get()
    now_node = now[1]
    if not visited[now_node]:
        visited[now_node] = True
        if now_node == end_point:
            break
        for next in A[now_node]:
            next_node = next[0]
            next_weight = next[1]
            if D[now_node] + next_weight < D[next_node]:
                D[next_node] = D[now_node] + next_weight
                q.put((D[next_node], next_node))

print(D[end_point])