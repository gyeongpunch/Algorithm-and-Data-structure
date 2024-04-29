import sys
input = sys.stdin.readline
from collections import deque

N, E = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = []
for _ in range(E):
    end, start = map(int, input().split())
    A[start].append(end)

def BFS(v):
    queue = deque()
    queue.append(v)
    cnt = 0

    visited = [False] * (N + 1)
    visited[v] = True

    while queue:
        now = queue.popleft()
        for next in A[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                cnt += 1
    return cnt


for i in range(1, N + 1):
    answer.append(BFS(i))

max1 = max(answer)
# print(max1)
# print(answer)
for i in range(N):
    if max1 == answer[i]:
        print(i + 1, end = ' ')