from collections import deque
import sys
input = sys.stdin.readline

n, e, start = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(e):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in A:
    i.sort()

def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in A[v]:
        if not visited[i]:
            DFS(i)
DFS(start)

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
visited = [False] * (n + 1)
BFS(start)