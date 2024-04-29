from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)

for i in range(1, N + 1):
    A[i].sort()

def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in A[v]:
        if not visited[i]:
            DFS(i)

DFS(V)
visited = [False] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()
BFS(V)