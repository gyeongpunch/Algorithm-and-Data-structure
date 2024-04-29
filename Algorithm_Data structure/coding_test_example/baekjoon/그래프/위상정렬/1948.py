import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
A = [[] for _ in range(n + 1)]
Reverse_A = [[] for _ in range(n + 1)]
D = [0] * (n + 1)

for i in range(m):
    start, end, length = map(int, input().split())
    A[start].append((end, length))
    Reverse_A[end].append((start, length))
    D[end] += 1

result_time = 0
result_road = 0

city = list(map(int, input().split()))

queue = deque()
queue.append(city[0])
result = [0] * (n + 1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        D[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])
        if D[next[0]] == 0:
            queue.append(next[0])

result_cnt = 0
visited = [False] * (n + 1)
queue.clear()
queue.append(city[1])
visited[city[1]] = True

while queue:
    now = queue.popleft()
    for next in Reverse_A[now]:
        if result[next[0]] + next[1] == result[now]:
            result_cnt += 1
            if not visited[next[0]]:
                queue.append(next[0])
                visited[next[0]] = True

print(result[city[1]])
print(result_cnt)