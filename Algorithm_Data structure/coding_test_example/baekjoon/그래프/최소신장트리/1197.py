import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, E = map(int, input().split())

pq = PriorityQueue()
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(E):
    start, end, length = map(int, input().split())
    pq.put((length, start, end))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N - 1:
    length, start, end = pq.get()
    # print(length, start, end)
    # useEdge += 1
    if find(start) != find(end):
        union(start, end)
        result += length
        useEdge += 1

print(result)