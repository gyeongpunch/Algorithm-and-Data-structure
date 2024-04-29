import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    start, end = map(int,input().split())
    A[start].append(end)
    A[end].append(start)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)