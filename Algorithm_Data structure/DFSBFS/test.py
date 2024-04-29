import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, e = map(int, input().split())

visited = [False] * (n + 1)
A = [[] for _ in range(n + 1)]

for i in range(e):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

def DFS(v):
    visited[v] = True
    print(v, "@@@@@@@@")
    for i in A[v]:
        if visited[i] == False:
            DFS(i)
            print(i, "@@@@@@@@")

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)
        

print(cnt)