import sys
input = sys.stdin.readline

n, e = map(int, input().split())
A = [[] for _ in range(n)]
visited = [False] * n

for _ in range(e):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)

arrived = False

def DFS(now, depth):
    global arrived
    visited[now] = True
    if depth == 5:
        arrived = True
        return
    for i in A[now]:
        if not visited[i]:
            visited[i] = True
            DFS(i, depth + 1)
    visited[now] = False

for i in range(n):
    DFS(i, 1)
    if arrived:
        break
if arrived:
    print(1)
else:
    print(0)