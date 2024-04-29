import sys
input = sys.stdin.readline
# from collections import deque

pc_n = int(input())
edge_n = int(input())
A = [[] for _ in range(pc_n + 1)]
visited = [False] * (pc_n + 1)

for i in range(edge_n):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)

def DFS(v):
    visited[v] = True
    global count
    count += 1
    for i in A[v]:
        if not visited[i]:
            DFS(i)


count = 0
DFS(1)
print(count - 1)
