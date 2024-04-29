import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, e = map(int, input().split())
data = [[] for _ in range(n + 1)]
answer = 0
visited = [False] * (n + 1)

for i in range(e):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

def DFS(now, depth):
    global answer
    if depth == 5:
        answer = 1
        return
    visited[now] = True
    for i in data[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False

for i in range(n):
    DFS(i, 1)
    if answer == 1:
        break
if answer == 1:
    print(1)
else:
    print(0)
