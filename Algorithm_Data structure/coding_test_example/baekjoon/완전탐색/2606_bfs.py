import sys
input = sys.stdin.readline
from collections import deque

pc_n = int(input())
edge_n = int(input())
A = [[] for _ in range(pc_n + 1)]
visited = [False] * (pc_n + 1)

for i in range(edge_n):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)

def BFS(v):
    queue = deque()
    count = 0
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count
print(BFS(1))