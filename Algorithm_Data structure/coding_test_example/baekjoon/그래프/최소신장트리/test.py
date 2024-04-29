import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())

pq = PriorityQueue()
parent = [0] * (V + 1)

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    start, end, weight = map(int, input().split())
    pq.put((weight, start, end))

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

Edge = 0
result = 0

while Edge < V - 1:
    weight, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += weight
        Edge += 1

print(result)