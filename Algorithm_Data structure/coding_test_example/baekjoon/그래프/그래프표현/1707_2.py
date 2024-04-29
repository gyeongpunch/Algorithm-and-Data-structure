import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
IsEven = True

def DFS(v):
    global IsEven
    visited[v] = True
    
    for i in A[v]:
        if visited[i] == 0:
            check[i] = not check[v]
            DFS(i)
        elif check[i] == check[v]:
            IsEven = False


for _ in range(T):
    N, E = map(int, input().split())
    A = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    check = [False] * (N + 1)
    IsEven = True
    for _ in range(E):
        start, end = map(int, input().split())
        A[start].append(end)
        A[end].append(start)

    for i in range(1, N + 1):
        if IsEven:
            DFS(i)
        else:
            break
    if IsEven:
        print('YES')
    else:
        print('NO')