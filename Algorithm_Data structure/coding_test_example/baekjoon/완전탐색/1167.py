import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
A = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    start = data[0]

    cnt = 1
    while data[cnt] != -1:
        A[start].append((data[cnt], data[cnt + 1]))
        cnt += 2
# print(A)
distance = [0] * (V + 1)
visited = [False] * (V + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                if distance[i[0]] < distance[now] + i[1]:
                    distance[i[0]] = distance[now] + i[1]

BFS(1)
Max = 1

for i in range(2, V + 1):
    if distance[Max] < distance[i]:
        Max = i

visited = [False] * (V + 1)
distance = [0] * (V + 1)
BFS(Max)
print(max(distance))

