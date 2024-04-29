import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
answer = []

for i in range(M):
    start, end = map(int, input().split())
    A[start].append(end)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)

BFS(X)

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)
if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)